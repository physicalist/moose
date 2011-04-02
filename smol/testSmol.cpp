/**********************************************************************
** This program is part of 'MOOSE', the
** Messaging Object Oriented Simulation Environment.
**           Copyright (C) 2003-2010 Upinder S. Bhalla. and NCBS
** It is made available under the terms of the
** GNU Lesser General Public License version 2.1
** See the file COPYING.LIB for the full notice.
**********************************************************************/

#include "SmolHeader.h"
#include "ElementValueFinfo.h"
#include "ReduceBase.h"
#include "ReduceMax.h"
#include "../shell/Shell.h"


// This is a regression test
void testSmoldynZombify( )
{
	cout << "." << flush;
}

void testCreateSmolSim()
{
	Eref sheller = Id().eref();
	Shell* shell = reinterpret_cast< Shell* >( sheller.data() );

	unsigned int size = 1;
	vector< unsigned int > dims( 1, size );
	Id smolId = shell->doCreate("SmolSim", Id(), "smol", dims );
	Id paId = shell->doCreate("Neutral", Id(), "pa", dims );
	Id mol1Id = shell->doCreate("Mol", paId, "mol1", dims );
	Id mol2Id = shell->doCreate("Mol", paId, "mol2", dims );
	Id reacId = shell->doCreate("Reac", paId, "reac", dims );

/*
	const Cinfo* sc = SmolSim::initCinfo();
	const Cinfo* mc = Mol::initCinfo();
	const Cinfo* rc = Reac::initCinfo();

	Id smolId = Id::nextId();
	Element* elm = new Element( smolId, sc, "smol", dims, 1 );
	assert( elm );

	Id mol1id = Id::nextId();
	Element* mol1 = new Element( mol1id, mc, "mol1", dims, 1 );
	Id mol2id = Id::nextId();
	Element* mol2 = new Element( mol2id, mc, "mol2", dims, 1 );
	Id reacId = Id::nextId();
	Element* reac = new Element( reacId, rc, "reac", dims, 1 );
	*/

	SmolSim* ss = reinterpret_cast< SmolSim* >( smolId.eref().data() );
	assert( ss );

	simstruct* sim = ss->sim_;
	assert( sim == 0 );

	ss->setPath( smolId.eref(), 0, "/pa/##" );

	delete smolId();
	delete paId();
	cout << "#" << flush;
}

void testSmoldyn()
{
	testCreateSmolSim();
}
