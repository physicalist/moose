/**********************************************************************
** This program is part of 'MOOSE', the
** Messaging Object Oriented Simulation Environment.
**           Copyright (C) 2003-2007 Upinder S. Bhalla. and NCBS
** It is made available under the terms of the
** GNU Lesser General Public License version 2.1
** See the file COPYING.LIB for the full notice.
**********************************************************************/

#include "header.h"
#include "HHGate.h"
#include "HHChannel.h"

const double HHChannel::EPSILON = 1.0e-10;
const int HHChannel::INSTANT_X = 1;
const int HHChannel::INSTANT_Y = 2;
const int HHChannel::INSTANT_Z = 4;

static SrcFinfo1< double > permeability( "permeability", 
	"Conductance term going out to GHK object" );
static SrcFinfo2< double, double > channelOut( "channelOut", 
	"Sends channel variables Gk and Ek to compartment" );
static SrcFinfo1< double > IkOut( "IkOut", 
	"Channel current. This message typically goes to concen"
	"objects that keep track of ion concentration." );

const Cinfo* HHChannel::initCinfo()
{
	/////////////////////////////////////////////////////////////////////
	// Shared messages
	/////////////////////////////////////////////////////////////////////
	static DestFinfo process( "process", 
		"Handles process call",
		new ProcOpFunc< HHChannel >( &HHChannel::process ) );
	static DestFinfo reinit( "reinit", 
		"Handles reinit call",
		new ProcOpFunc< HHChannel >( &HHChannel::reinit ) );
	static Finfo* processShared[] =
	{
		&process, &reinit
	};
	static SharedFinfo proc( "proc", 
			"This is a shared message to receive Process message from the"
			"scheduler. The first entry is a MsgDest for the Process "
			"operation. It has a single argument, ProcInfo, which "
			"holds lots of information about current time, thread, dt and"
			"so on.\n The second entry is a MsgDest for the Reinit "
			"operation. It also uses ProcInfo.",
		processShared, sizeof( processShared ) / sizeof( Finfo* )
	);

	/////////////////////////////////////////////////////////////////////
	/// ChannelOut SrcFinfo defined above.
	static DestFinfo Vm( "Vm", 
		"Handles Vm message coming in from compartment",
		new OpFunc1< HHChannel, double >( &HHChannel::handleVm ) );

	static Finfo* channelShared[] =
	{
		&channelOut, &Vm
	};
	static SharedFinfo channel( "channel", 
		"This is a shared message to couple channel to compartment. "
		"The first entry is a MsgSrc to send Gk and Ek to the compartment "
		"The second entry is a MsgDest for Vm from the compartment.",
		channelShared, sizeof( channelShared ) / sizeof( Finfo* )
	);

	/////////////////////////////////////////////////////////////////////
	/*
	* All the Gate messages are now eliminated. Will use FieldElements
	* directly, instead.
	static Finfo* xGateShared[] =
	{
		new SrcFinfo( "Vm", Ftype1< double >::global() ),
		new DestFinfo( "gate", Ftype2< double, double >::global(),
				RFCAST( &HHChannel::xGateFunc ) ),
	};

	static Finfo* yGateShared[] =
	{
		new SrcFinfo( "Vm", Ftype1< double >::global() ),
		new DestFinfo( "gate", Ftype2< double, double >::global(),
				RFCAST( &HHChannel::yGateFunc ) ),
	};

	static Finfo* zGateShared[] =
	{
		new SrcFinfo( "Vm", Ftype1< double >::global() ),
		new DestFinfo( "gate", Ftype2< double, double >::global(),
			RFCAST( &HHChannel::zGateFunc ) ),
	};
		new SharedFinfo( "xGate", xGateShared,
			sizeof( xGateShared ) / sizeof( Finfo* ),
			"This is a shared message to communicate with the X gate. "
			"Sends out Vm. "
			"Receives lookedup up values A and B for the Vm. "
			"The A term is the alpha term from HH equations. "
			"The B term is actually alpha + beta, precalculated. " ),
		new SharedFinfo( "yGate", yGateShared,
			sizeof( yGateShared ) / sizeof( Finfo* ),
			"Shared message for Y gate. Fields as in X gate."),
		new SharedFinfo( "zGate", zGateShared,
			sizeof( zGateShared ) / sizeof( Finfo* ),
			"Shared message for Z gate. Fields as in X gate."),
		*/

	///////////////////////////////////////////////////////
	// Here we reuse the Vm DestFinfo declared above.

	/// Permability SrcFinfo defined above.
	static Finfo* ghkShared[] =
	{
		&Vm, &permeability
	};
	static SharedFinfo ghk( "ghk", 
		"Message to Goldman-Hodgkin-Katz object",
		ghkShared, sizeof( ghkShared ) / sizeof( Finfo* ) );

///////////////////////////////////////////////////////
// Field definitions
///////////////////////////////////////////////////////

		static ValueFinfo< HHChannel, double > Gbar( "Gbar",
			"Maximal channel conductance",
			&HHChannel::setGbar,
			&HHChannel::getGbar
		);
		static ValueFinfo< HHChannel, double > Ek( "Ek", 
			"Reversal potential of channel",
			&HHChannel::setEk,
			&HHChannel::getEk
		);
		static ValueFinfo< HHChannel, double > Xpower( "Xpower",
			"Power for X gate",
			&HHChannel::setXpower,
			&HHChannel::getXpower
		);
		static ValueFinfo< HHChannel, double > Ypower( "Ypower",
			"Power for Y gate",
			&HHChannel::setYpower,
			&HHChannel::getYpower
		);
		static ValueFinfo< HHChannel, double > Zpower( "Zpower",
			"Power for Z gate",
			&HHChannel::setZpower,
			&HHChannel::getZpower
		);
		static ValueFinfo< HHChannel, int > instant( "instant",
			"Bitmapped flag: bit 0 = Xgate, bit 1 = Ygate, bit 2 = Zgate"
			"When true, specifies that the lookup table value should be"
			"used directly as the state of the channel, rather than used"
			"as a rate term for numerical integration for the state",
			&HHChannel::setInstant,
			&HHChannel::getInstant
		);
		static ValueFinfo< HHChannel, double > Gk( "Gk",
			"Channel conductance variable",
			&HHChannel::setGk,
			&HHChannel::getGk
		);
		static ReadOnlyValueFinfo< HHChannel, double > Ik( "Ik",
			"Channel current variable",
			&HHChannel::getIk
		);
		static ValueFinfo< HHChannel, double > X( "X", 
			"State variable for X gate",
			&HHChannel::setX,
			&HHChannel::getX
		);
		static ValueFinfo< HHChannel, double > Y( "Y",
			"State variable for Y gate",
			&HHChannel::setY,
			&HHChannel::getY
		);
		static ValueFinfo< HHChannel, double > Z( "Z",
			"State variable for Y gate",
			&HHChannel::setZ,
			&HHChannel::getZ
		);
		static ValueFinfo< HHChannel, int > useConcentration( 
			"useConcentration",
			"Flag: when true, use concentration message rather than Vm to"
			"control Z gate",
			&HHChannel::setUseConcentration,
			&HHChannel::getUseConcentration
		);

///////////////////////////////////////////////////////
// MsgSrc definitions
///////////////////////////////////////////////////////
	// IkOut SrcFinfo defined above.

///////////////////////////////////////////////////////
// MsgDest definitions
///////////////////////////////////////////////////////
		static DestFinfo concen( "concen", 
			"Incoming message from Concen object to specific conc to use"
			"in the Z gate calculations",
			new OpFunc1< HHChannel, double >( &HHChannel::handleConc )
		);
		static DestFinfo createGate( "createGate",
			"Function to create specified gate."
			"Argument: Gate type [X Y Z]",
			new OpFunc1< HHChannel, string >( &HHChannel::createGateFunc )
		);
	static Finfo* HHChannelFinfos[] =
	{
		&proc,				// Shared
		&channel,			// Shared
		&ghk,				// Shared
		&Gbar,				// Value
		&Ek,				// Value
		&Xpower,			// Value
		&Ypower,			// Value
		&Zpower,			// Value
		&instant,			// Value
		&Gk,				// Value
		&Ik,				// ReadOnlyValue
		&X,					// Value
		&Y,					// Value
		&Z,					// Value
		&useConcentration,	// Value
		&IkOut,				// Src
		&concen,			// Dest
		&createGate,		// Dest
	};
	
	static string doc[] =
	{
		"Name", "HHChannel",
		"Author", "Upinder S. Bhalla, 2007, NCBS",
		"Description", "HHChannel: Hodgkin-Huxley type voltage-gated Ion channel. Something "
		"like the old tabchannel from GENESIS, but also presents "
		"a similar interface as hhchan from GENESIS. ",
	};

	static Cinfo HHChannelCinfo(
		"HHChannel",
		Neutral::initCinfo(),
		HHChannelFinfos,
		sizeof( HHChannelFinfos )/sizeof(Finfo *),
		new Dinfo< HHChannel >()
	);

	return &HHChannelCinfo;
}

static const Cinfo* hhChannelCinfo = HHChannel::initCinfo();
//////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////
// Constructor
///////////////////////////////////////////////////
HHChannel::HHChannel()
			: Xpower_( 0.0 ), Ypower_( 0.0 ), Zpower_( 0.0 ),
			Vm_( 0.0 ), conc_( 0.0 ),
			Gbar_( 0.0 ), Ek_( 0.0 ),
			instant_( 0 ),
			Gk_( 0.0 ), Ik_( 0.0 ),
			X_( 0.0 ), Y_( 0.0 ), Z_( 0.0 ),
            xInited_( false ), yInited_( false ), zInited_( false ),
			g_( 0.0 ),
			useConcentration_( 0 )
{
	;
}

///////////////////////////////////////////////////
// Virtual function definitions
///////////////////////////////////////////////////
/*
void HHChannel::lookupXrates( Eref e )
{
	send1< double >( e, xGateSlot, Vm_ );
}

void HHChannel::lookupYrates( Eref e )
{
	send1< double >( e, yGateSlot, Vm_ );
}

void HHChannel::lookupZrates( Eref e )
{
	if ( useConcentration_ )
		send1< double >( e, zGateSlot, conc_ );
	else
		send1< double >( e, zGateSlot, Vm_ );
}
*/

/**
 * Assigns the Xpower for this gate. If the gate exists and has
 * only this element for input, then change the gate value.
 * If the gate exists and has multiple parents, then make a new gate.
 * If the gate does not exist, make a new gate
 */
void HHChannel::setXpower( double Xpower )
{
	if ( Xpower == Xpower_ )
		return;
	
	Xpower_ = Xpower;
	takeXpower_ = selectPower( Xpower );
	
	if ( Xpower == 0.0 ) {
		destroyGate( "X" );
		return;
	}
}

void HHChannel::setYpower( double Ypower )
{
	if ( Ypower == Ypower_ )
		return;
	
	Ypower_ = Ypower;
	takeYpower_ = selectPower( Ypower );
	
	if ( Ypower == 0.0 ) {
		destroyGate( "Y" );
		return;
	}
}

void HHChannel::setZpower( double Zpower )
{
	if ( Zpower == Zpower_ )
		return;
	
	Zpower_ = Zpower;
	takeZpower_ = selectPower( Zpower );
	useConcentration_ = 1;
	
	if ( Zpower == 0.0 ) {
		destroyGate("Z" );
		return;
	}
}

/**
 * If the gate exists and has only this element for input, then change
 * the gate power.
 * If the gate exists and has multiple parents, then make a new gate,
 * 	set its power.
 * If the gate does not exist, make a new gate, set its power.
 *
 * The function is designed with the idea that if copies of this
 * channel are made, then they all point back to the original HHGate.
 * (Unless they are cross-node copies).
 * It is only if we subsequently alter the HHGate of this channel that
 * we need to make our own variant of the HHGate, or disconnect from
 * an existing one.
 * \todo: May need to convert to handling arrays and Erefs.
 */
// Assuming that the elements are simple elements. Use Eref for 
// general case
void HHChannel::createGateFunc( string gateType )
{
	string name;
	if ( gateType == "X" )
		name = "xGate";
	else if ( gateType == "Y" )
		name = "yGate";
	else if ( gateType == "Z" )
		name = "zGate";
	else
		assert( 0 );
	
	/*
	 * Calling a few virtual functions.
	 * 
	 * chanFinfo: The finfo on HHChannel that connects to a gate
	 * gateFinfo: The finfo on HHGate that connects to a channel
	 * gateClass: "HHGate" or "HHGate2D"
	string chanFinfo = chanFinfo( gateType );
	string gateFinfo = gateFinfo( gateType );
	string gateClass = gateClass( gateType );
	
	Element* gate = 0;
	Eref e = c->target();
	const Finfo* f = e->findFinfo( chanFinfo );
	unsigned int numGates = e->msg( f->msg() )->numTargets( e.e );
	assert( numGates <= 1 );
	
	if ( numGates == 1 ) {
		Conn* gateConn = e->targets( f->msg(), 0 ); // zero index for SE
		Element* existingGate = gateConn->target().e;
		delete gateConn;
		unsigned int numChans =
			existingGate->msg( existingGate->findFinfo( gateFinfo )->msg() )->size();
		
		assert( numChans > 0 );
		if ( numChans > 1 ) {
			// Here we have multiple channels using this gate. So
			// we don't mess with the original.
			// make a new gate which we can change.
			gate = Neutral::create( gateClass, name, e->id(), idGen.next() );
			gate->addFinfo( GlobalMarkerFinfo::global() );
                        Eref(e).dropAll(chanFinfo);
			bool ret = Eref( e ).add( chanFinfo, gate, gateFinfo );
			assert( ret );
		}
	} else { // No gate, make a new one.
		gate = Neutral::create( gateClass, name, e->id(), idGen.next() );
		// Make it a global so that duplicates do not happen unless
		// the table values change.
		gate->addFinfo( GlobalMarkerFinfo::global() );
		bool ret = Eref( e ).add( chanFinfo, gate, gateFinfo );
		assert( ret );
	}
	
	// If a gate was created in this function, then create interpols inside it.
	if ( gate != 0 ) {
		string path = e->id().path() + "/" + name;
		assert( Id( path ).good() );
		
		set< IdGenerator >( gate, "createInterpols", idGen );
		assert( Id( path + "/A" ).good() );
		assert( Id( path + "/B" ).good() );
	}
	 */
}

void HHChannel::destroyGate( string gateType )
{
	/*
	HHChannel* ch = static_cast< HHChannel* >( e.data() );
	string chanFinfo = ch->chanFinfo( gateType );
	string gateFinfo = ch->gateFinfo( gateType );
	
	Element* gate = 0;
	const Finfo* f = e->findFinfo( chanFinfo );
	Conn* gateConn = e->targets( f->msg(), 0 ); // zero index for SE
	unsigned int numGates = e->msg( f->msg() )->numTargets( e.e );
	assert( numGates <= 1 );
	
	// If gate exists, remove it.
	if ( numGates == 1 ) {
		gate = gateConn->target().e;
		unsigned int numChans =
			gate->msg( gate->findFinfo( gateFinfo )->msg() )->size();
		assert( numChans > 0 );
		if ( numChans > 1 ) {
			// Here we have multiple channels using this gate. So
			// we don't mess with the original.
			// Get rid of local connection to gate, but don't delete
			Eref( e ).dropAll( f->msg() );
		} else { // Delete the single gate.
			bool ret = set( gate, "destroy" );
			assert( ret );
		}
	}
	*/
}

///////////////////////////////////////////////////
// Field function definitions
///////////////////////////////////////////////////

void HHChannel::setGbar( double Gbar )
{
	Gbar_ = Gbar;
}
double HHChannel::getGbar() const
{
	return Gbar_;
}

void HHChannel::setEk( double Ek )
{
	Ek_ = Ek;
}
double HHChannel::getEk() const
{
	return Ek_;
}

/**
 * Assigns the Xpower for this gate. If the gate exists and has
 * only this element for input, then change the gate value.
 * If the gate exists and has multiple parents, then make a new gate.
 * If the gate does not exist, make a new gate
 */

double HHChannel::getXpower() const
{
	return Xpower_;
}

double HHChannel::getYpower() const
{
	return Ypower_;
}

double HHChannel::getZpower() const
{
	return Zpower_;
}

void HHChannel::setInstant( int instant )
{
	instant_ = instant;
}
int HHChannel::getInstant() const
{
	return instant_;
}

void HHChannel::setGk( double Gk )
{
	Gk_ = Gk;
}
double HHChannel::getGk() const
{
	return Gk_;
}

double HHChannel::getIk() const
{
	return Ik_;
}

void HHChannel::setX( double X )
{
        X_ = X;
        xInited_ = true;        
}
double HHChannel::getX() const
{
	return X_;
}

void HHChannel::setY( double Y )
{
        Y_ = Y;
        yInited_ = true;        
}
double HHChannel::getY() const
{
	return Y_;
}

void HHChannel::setZ( double Z )
{
        Z_ = Z;
        zInited_ = true;        
}
double HHChannel::getZ() const
{
	return Z_;
}

void HHChannel::setUseConcentration( int value )
{
	useConcentration_ = value;
}

int HHChannel::getUseConcentration() const
{
	return useConcentration_;
}

///////////////////////////////////////////////////
// Dest function definitions
///////////////////////////////////////////////////

/**
 * Returns the state variable for the new timestep based on
 * the internal variables A_ and B_ which were passed in from the gate.
 */
double HHChannel::integrate( double state, double dt, double A, double B )
{
	if ( B_ > EPSILON ) {
		double x = exp( -B * dt );
		return state * x + ( A / B ) * ( 1 - x );
	}
	return state + A * dt ;
}

void HHChannel::process( const Eref& e, ProcPtr info )
{
	g_ += Gbar_;
	double A = 0;
	double B = 0;
	if ( Xpower_ > 0 ) {
		xGate_->lookupBoth( Vm_, &A, &B );
		if ( instant_ & INSTANT_X )
			X_ = A/B;
		else 
			X_ = integrate( X_, info->dt, A, B );
		g_ *= takeXpower_( X_, Xpower_ );
	}

	if ( Ypower_ > 0 ) {
		yGate_->lookupBoth( Vm_, &A, &B );
		if ( instant_ & INSTANT_Y )
			Y_ = A/B;
		else 
			Y_ = integrate( Y_, info->dt, A, B );

		g_ *= takeYpower_( Y_, Ypower_ );
	}

	if ( Zpower_ > 0 ) {
		if ( useConcentration_ )
			zGate_->lookupBoth( conc_, &A, &B );
		else
			zGate_->lookupBoth( Vm_, &A, &B );
		if ( instant_ & INSTANT_Z )
			Z_ = A/B;
		else 
			Z_ = integrate( Z_, info->dt, A, B );

		g_ *= takeZpower_( Z_, Zpower_ );
	}

	Gk_ = g_;
	channelOut.send( e, info, Gk_, Ek_ );
	Ik_ = ( Ek_ - Vm_ ) * g_;
	
	// This is used if the channel connects up to a conc pool and
	// handles influx of ions giving rise to a concentration change.
	IkOut.send( e, info, Ik_ );
	
	// Needed by GHK-type objects
	permeability.send( e, info, Gk_ );
	
	g_ = 0.0;
}

/**
 * Here we get the steady-state values for the gate (the 'instant'
 * calculation) as A_/B_.
 */
void HHChannel::reinit( const Eref& er, ProcPtr info )
{
	g_ = Gbar_;
	Element* e = er.element();

	double A = 0.0;
	double B = 0.0;
	if ( Xpower_ > 0 ) {
		xGate_->lookupBoth( Vm_, &A, &B );
		if ( B < EPSILON ) {
			cout << "Warning: B_ value for " << e->getName() <<
					" is ~0. Check X table\n";
			return;
		}
                if (!xInited_)
                    X_ = A/B;
		g_ *= takeXpower_( X_, Xpower_ );
	}

	if ( Ypower_ > 0 ) {
		yGate_->lookupBoth( Vm_, &A, &B );
		if ( B < EPSILON ) {
			cout << "Warning: B value for " << e->getName() <<
					" is ~0. Check Y table\n";
			return;
		}
                if (!yInited_)
                    Y_ = A/B;
		g_ *= takeYpower_( Y_, Ypower_ );
	}

	if ( Zpower_ > 0 ) {
		if ( useConcentration_ )
			zGate_->lookupBoth( conc_, &A, &B );
		else
			zGate_->lookupBoth( Vm_, &A, &B );
		if ( B < EPSILON ) {
			cout << "Warning: B value for " << e->getName() <<
					" is ~0. Check Z table\n";
			return;
		}
                if (!zInited_)
                    Z_ = A/B;
		g_ *= takeZpower_( Z_, Zpower_ );
	}

	Gk_ = g_;

	channelOut.send( er, info, Gk_, Ek_ );
	// channelSrc_.send( Gk_, Ek_ );
	Ik_ = ( Ek_ - Vm_ ) * g_;
	
	// Needed by GHK-type objects
	permeability.send( er, info, Gk_ );
	
	g_ = 0.0;
}

void HHChannel::handleVm( double Vm )
{
	Vm_ = Vm;
}

void HHChannel::handleConc( double conc )
{
	conc_ = conc;
}

void HHChannel::xGateFunc( double A, double B )
{
	A_ = A;
	B_ = B;
}

void HHChannel::yGateFunc( double A, double B )
{
	A_ = A;
	B_ = B;
}

void HHChannel::zGateFunc( double A, double B )
{
	A_ = A;
	B_ = B;
}

///////////////////////////////////////////////////
// Utility function
///////////////////////////////////////////////////
double HHChannel::powerN( double x, double p )
{
	if ( x > 0.0 )
		return exp( p * log( x ) );
	return 0.0;
}

PFDD HHChannel::selectPower( double power )
{
	if ( power == 0.0 )
		return powerN;
	else if ( power == 1.0 )
		return power1;
	else if ( power == 2.0 )
		return power2;
	else if ( power == 3.0 )
		return power3;
	else if ( power == 4.0 )
		return power4;
	else
		return powerN;
}

///////////////////////////////////////////////////
// Unit tests
///////////////////////////////////////////////////

#ifdef DO_UNIT_TESTS
#include "ReduceBase.h"
#include "ReduceMax.h"
#include "../shell/Shell.h"
#include "Compartment.h"

static const double EREST = -0.07;

// AP measured in millivolts wrt EREST, at a sample interval of 
// 100 usec
static double actionPotl[] = { 0,
1.2315, 2.39872, 3.51917, 4.61015, 5.69088, 6.78432, 7.91934, 9.13413,
10.482, 12.0417, 13.9374, 16.3785, 19.7462, 24.7909, 33.0981, 47.967,
73.3833, 98.7377, 105.652, 104.663, 101.815, 97.9996, 93.5261, 88.6248,
83.4831, 78.2458, 73.0175, 67.8684, 62.8405, 57.9549, 53.217, 48.6206,
44.1488, 39.772, 35.4416, 31.0812, 26.5764, 21.7708, 16.4853, 10.6048,
4.30989, -1.60635, -5.965, -8.34834, -9.3682, -9.72711,
-9.81085, -9.78371, -9.71023, -9.61556, -9.50965, -9.39655,
-9.27795, -9.15458, -9.02674, -8.89458, -8.75814, -8.61746,
-8.47254, -8.32341, -8.17008, -8.01258, -7.85093, -7.68517,
-7.51537, -7.34157, -7.16384, -6.98227, -6.79695, -6.60796,
-6.41542, -6.21944, -6.02016, -5.81769, -5.61219, -5.40381,
-5.19269, -4.979, -4.76291, -4.54459, -4.32422, -4.10197,
-3.87804, -3.65259, -3.42582, -3.19791, -2.96904, -2.7394,
-2.50915, -2.27848, -2.04755, -1.81652, -1.58556, -1.3548,
-1.12439, -0.894457, -0.665128, -0.436511, -0.208708, 0.0181928,
};

void lset( 
	Element* gate, const Finfo* table, double val, unsigned int i )
{
	// lookupSet< double, unsigned int >( gate, table, val, i );
}

double Na_m_A( double v )
{
	if ( fabs( EREST + 0.025 - v ) < 1e-6 )
		v += 1e-6;
	return  0.1e6 * ( EREST + 0.025 - v ) / ( exp ( ( EREST + 0.025 - v )/ 0.01 ) - 1.0 );
}

double Na_m_B( double v )
{
	return 4.0e3 * exp ( ( EREST - v ) / 0.018 );
}

double Na_h_A( double v )
{
	return 70.0 * exp ( ( EREST - v ) / 0.020 );
}

double Na_h_B( double v )
{
	return 1.0e3 / ( exp ( ( 0.030 + EREST - v )/ 0.01 )  + 1.0 );
}

double K_n_A( double v )
{
	if ( fabs( EREST + 0.025 - v ) < 1e-6 )
		v += 1e-6;
	
	return ( 1.0e4 * ( 0.01 + EREST - v ) ) / ( exp ( ( 0.01 + EREST         - v ) / 0.01 ) - 1.0 );
}

double K_n_B( double v )
{
	return 0.125e3 * exp ( (EREST - v ) / 0.08 );
}

void testHHChannel()
{
	Shell* shell = reinterpret_cast< Shell* >( ObjId( Id(), 0 ).data() );
	cout << "\nTesting HHChannel";
	vector< unsigned int > dims( 1, 1 );
	Id nid = shell->doCreate( "Neutral", Id(), "n", dims );
	Id comptId = shell->doCreate( "Compartment", nid, "compt", dims );
	Id chanId = shell->doCreate( "HHChannel", nid, "Na", dims );
	MsgId mid = shell->doAddMsg( "Single", ObjId( comptId ), "channel", 
		ObjId( chanId ), "channel" );
	assert( mid != Msg::badMsg );
	
	// Check gate construction and removal when powers are assigned
	/*
	Slot childSlot = initHHChannelCinfo()->getSlot( "childSrc" );

	ASSERT( ret, "Setting up channel" );

	// ASSERT( compt->findFinfo( "channel" )->add( compt, chan, chan->findFinfo( "channel" ) ), "Setting up channel" );

	
	ASSERT( chan->msg( childSlot.msg() )->size() == 0, "Creating xGate");
	set< double >( chan, "Xpower", 2.0 );
	ASSERT( chan->msg( xGateSlot.msg() )->size() == 1, "Creating xGate");
	ASSERT( chan->msg( childSlot.msg() )->size() == 1, "Creating xGate");

	set< double >( chan, "Xpower", 0.0 );
	ASSERT( chan->msg( childSlot.msg() )->size() == 0, "Removing xGate");
	ASSERT( chan->msg( xGateSlot.msg() )->size() == 0, "Removing xGate");
	set< double >( chan, "Xpower", 3.0 );
	ASSERT( chan->msg( xGateSlot.msg() )->size() == 1, "Creating xGate again");

	Id xGateId;
	ret = lookupGet< Id, string >(
		chan, "lookupChild", xGateId, "xGate" );
	ASSERT( ret, "Look up xGate");
	ASSERT( !xGateId.zero() && !xGateId.bad(), "Lookup xGate" );

	Element* xGate = xGateId();

	set< double >( chan, "Ypower", 1.0 );
	ASSERT( chan->msg( yGateSlot.msg() )->size() == 1, "Creating yGate");
	
	// Check steady-state calculation for channel cond on reinit
	// Here we start with Gbar = 1, Vm set ahead of time to 0,
	// xGate giving an X_ state of 2 and yGate of 10 for Vm == 0.
	Id temp;

	////////////////////////////////////////////////////////////////
	// Set up X gates
	////////////////////////////////////////////////////////////////
	// Set up X gate A
	ret = lookupGet< Id, string >( xGate, "lookupChild", temp, "A" );
	ASSERT( ret, "Check gate table" );
	ASSERT( !temp.zero() && !temp.bad(), "xGate_A" );
	Element* xGate_A = temp();
	set< double >( xGate_A, "xmin", -2.0 );
	set< double >( xGate_A, "xmax", 2.0 );
	set< int >( xGate_A, "xdivs", 1 );
	lookupSet< double, unsigned int >( xGate_A, "table", 0.0, 0 );
	lookupSet< double, unsigned int >( xGate_A, "table", 4.0, 1 );

	// Set up X gate B
	ret = lookupGet< Id, string >( xGate, "lookupChild", temp, "B" );
	ASSERT( ret, "Check gate table" );
	ASSERT( !temp.zero() && !temp.bad(), "xGate_B" );
	Element* xGate_B = temp();
	set< double >( xGate_B, "xmin", -1.0 );
	set< double >( xGate_B, "xmax", 1.0 );
	set< int >( xGate_B, "xdivs", 1 );
	lookupSet< double, unsigned int >( xGate_B, "table", 0.0, 0 );
	lookupSet< double, unsigned int >( xGate_B, "table", 2.0, 1 );

	////////////////////////////////////////////////////////////////
	// Set up Y gates
	////////////////////////////////////////////////////////////////
	Id yGateId;
	ret = lookupGet< Id, string >( chan, "lookupChild", yGateId, "yGate" );
	ASSERT( ret, "Look up yGate");
	ASSERT( !yGateId.zero() && !yGateId.bad(), "Lookup yGate" );

	Element* yGate = yGateId();
	ret = lookupGet< Id, string >( yGate, "lookupChild", temp, "A" );
	ASSERT( ret, "Check gate table" );
	ASSERT( !temp.zero() && !temp.bad(), "yGate_A" );
	Element* yGate_A = temp();
	set< double >( yGate_A, "xmin", -2.0 );
	set< double >( yGate_A, "xmax", 2.0 );
	set< int >( yGate_A, "xdivs", 1 );
	lookupSet< double, unsigned int >( yGate_A, "table", 20.0, 0 );
	lookupSet< double, unsigned int >( yGate_A, "table", 0.0, 1 );

	ret = lookupGet< Id, string >( yGate, "lookupChild", temp, "B" );
	ASSERT( ret, "Check gate table" );
	ASSERT( !temp.zero() && !temp.bad(), "yGate_B" );
	Element* yGate_B = temp();
	set< double >( yGate_B, "xmin", -1.0 );
	set< double >( yGate_B, "xmax", 1.0 );
	set< int >( yGate_B, "xdivs", 1 );
	lookupSet< double, unsigned int >( yGate_B, "table", 0.0, 0 );
	lookupSet< double, unsigned int >( yGate_B, "table", 2.0, 1 );

	////////////////////////////////////////////////////////////////
	// Do the Reinit.
	////////////////////////////////////////////////////////////////
	set< double >( chan, "Gbar", 1.0 );
	set< double >( chan, "Ek", 0.0 );
	ProcInfo pb;
	pb.dt = 0.001;
	SetConn c( chan, 0 );
	HHChannel* Na = static_cast< HHChannel* >( c.data() );
	Na->Vm_ = 0.0;

	// This function should do all the reinit steps.
	HHChannel::reinitFunc( &c, &pb );
	ASSERT( Na->Gk_ == 80, "Gk_" );
	ASSERT( Na->X_ == 2, "X_" );
	ASSERT( Na->Y_ == 10, "Y_" );

	////////////////////////////////////////////////////////////////
	// Check construction and result of HH squid simulation
	////////////////////////////////////////////////////////////////
	
	Element* kchan = Neutral::create( "HHChannel", "K", compt->id(), 
		Id::scratchId() );

	ret = Eref( compt ).add( "channel", kchan, "channel" );
	ASSERT( ret, "Setting up K channel" );

	// ASSERT( compt->findFinfo( "channel" )->add( compt, kchan, kchan->findFinfo( "channel" ) ), "Setting up K channel" );

	static const double VMIN = -0.1;
	static const double VMAX = 0.05;
	static const unsigned int XDIVS = 150;

	set< double >( compt, "Cm", 0.007854e-6 );
	set< double >( compt, "Ra", 7639.44e3 ); // does it matter?
	set< double >( compt, "Rm", 424.4e3 );
	set< double >( compt, "Em", EREST + 0.010613 );
	set< double >( compt, "inject", 0.1e-6 );
	set< double >( chan, "Gbar", 0.94248e-3 );
	set< double >( chan, "Ek", EREST + 0.115 );
	set< double >( kchan, "Gbar", 0.282743e-3 );
	set< double >( kchan, "Ek", EREST - 0.012 );
	set< double >( kchan, "Xpower", 4.0 );

	Id kGateId;
	ret = lookupGet< Id, string >( kchan, "lookupChild", kGateId, "xGate" );
	ASSERT( ret, "Look up kGate");
	ASSERT( !kGateId.zero() && !kGateId.bad(), "Lookup kGate" );

	Element* kGate = kGateId();
	ret = lookupGet< Id, string >( kGate, "lookupChild", temp, "A" );
	ASSERT( ret, "Check gate table" );
	ASSERT( !temp.zero() && !temp.bad(), "kGate_A" );
	Element* kGate_A = temp();
	ret = lookupGet< Id, string >( kGate, "lookupChild", temp, "B" );
	ASSERT( ret, "Check gate table" );
	ASSERT( !temp.zero() && !temp.bad(), "kGate_B" );
	Element* kGate_B = temp();

	ret = set< double >( xGate_A, "xmin", VMIN ) ; assert( ret );
	ret = set< double >( xGate_B, "xmin", VMIN ) ; assert( ret );
	ret = set< double >( yGate_A, "xmin", VMIN ) ; assert( ret );
	ret = set< double >( yGate_B, "xmin", VMIN ) ; assert( ret );
	ret = set< double >( kGate_A, "xmin", VMIN ) ; assert( ret );
	ret = set< double >( kGate_B, "xmin", VMIN ) ; assert( ret );

	ret = set< double >( xGate_A, "xmax", VMAX ) ; assert( ret );
	ret = set< double >( xGate_B, "xmax", VMAX ) ; assert( ret );
	ret = set< double >( yGate_A, "xmax", VMAX ) ; assert( ret );
	ret = set< double >( yGate_B, "xmax", VMAX ) ; assert( ret );
	ret = set< double >( kGate_A, "xmax", VMAX ) ; assert( ret );
	ret = set< double >( kGate_B, "xmax", VMAX ) ; assert( ret );

	ret = set< int >( xGate_A, "xdivs", XDIVS ) ; assert( ret );
	ret = set< int >( xGate_B, "xdivs", XDIVS ) ; assert( ret );
	ret = set< int >( yGate_A, "xdivs", XDIVS ) ; assert( ret );
	ret = set< int >( yGate_B, "xdivs", XDIVS ) ; assert( ret );
	ret = set< int >( kGate_A, "xdivs", XDIVS ) ; assert( ret );
	ret = set< int >( kGate_B, "xdivs", XDIVS ) ; assert( ret );

	ret = set< int >( xGate_A, "mode", 1 ) ; assert( ret );
	ret = set< int >( xGate_B, "mode", 1 ) ; assert( ret );
	ret = set< int >( yGate_A, "mode", 1 ) ; assert( ret );
	ret = set< int >( yGate_B, "mode", 1 ) ; assert( ret );
	ret = set< int >( kGate_A, "mode", 1 ) ; assert( ret );
	ret = set< int >( kGate_B, "mode", 1 ) ; assert( ret );

	double v = VMIN;
	double dv = ( VMAX - VMIN ) / XDIVS;
	const Finfo* table = xGate_A->findFinfo( "table" );
	for (unsigned int i = 0 ; i <= XDIVS; i++ ) {
		lset( xGate_A, table, Na_m_A( v ), i );
		lset( xGate_B, table, Na_m_A( v ) + Na_m_B( v ), i );
		lset( yGate_A, table, Na_h_A( v ), i );
		lset( yGate_B, table, Na_h_A( v ) + Na_h_B( v ), i );
		lset( kGate_A, table, K_n_A( v ), i );
		lset( kGate_B, table, K_n_A( v ) + K_n_B( v ), i );
		v = v + dv;
	}

	ret = set< double >( compt, "initVm", EREST ); assert( ret );

	pb.dt = 1.0e-5;
	pb.currTime_ = 0.0;
	SetConn c1( compt, 0 );
	SetConn c2( chan, 0 );
	SetConn c3( kchan, 0 );

	moose::Compartment::reinitFunc( &c1, &pb );
	HHChannel::reinitFunc( &c2, &pb );
	HHChannel::reinitFunc( &c3, &pb );

	unsigned int sample = 0;
	double delta = 0.0;
	for ( pb.currTime_ = 0.0; pb.currTime_ < 0.01;
			pb.currTime_ += pb.dt )
	{
		moose::Compartment::processFunc( &c1, &pb );
		HHChannel::processFunc( &c2, &pb );
		HHChannel::processFunc( &c3, &pb );
		if ( static_cast< int >( pb.currTime_ * 1e5 ) % 10 == 0 ) {
			get< double >( compt, "Vm", v );
			// cout << v << endl;
			v -= EREST + actionPotl[ sample++ ] * 0.001;
			delta += v * v;
		}
	}

	ASSERT( delta < 5e-4, "Action potl unit test\n" );
	
	////////////////////////////////////////////////////////////////
	// Clear it all up
	////////////////////////////////////////////////////////////////
	*/
	shell->doDelete( nid );
	cout << "." << flush;
}
#endif 
