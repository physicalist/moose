using System;
using System.Runtime.InteropServices;
 
/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.4
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

namespace libsbmlcs {

 using System;
 using System.Runtime.InteropServices;

/** 
 * @sbmlpackage{core}
 *
@htmlinclude pkg-marker-core.html An SBML <em>assignment rule</em> representing <em>x = f(<b>Y</b>)</em>.
 *
 * The rule type AssignmentRule is derived from the parent class Rule.  It
 * is used to express equations that set the values of variables.  The
 * left-hand side (the attribute named 'variable') of an assignment rule
 * can refer to the identifier of a Species, SpeciesReference (in SBML
 * Level&nbsp;3), Compartment, or Parameter
 * @if conly structure @else object@endif in the model (but not a
 * Reaction).  The entity identified must have its 'constant' attribute set
 * to @c false.  The effects of an assignment rule construct are in general
 * terms the same, but differ in the precise details depending on the type of
 * SBML component being set:
 * <ul>
 *
 * <li> <em>In the case of a species</em>, an SBML assignment rule sets the
 * referenced species' quantity (whether a 'concentration' or 'amount') to
 * the value determined by the formula in the MathML subelement 'math'.
 * The unit associated with the value produced by the 'math' formula @em
 * should (in SBML Level&nbsp;2 Version&nbsp;4 and in SBML Level&nbsp;3) or @em must (in
 * SBML releases prior to Level&nbsp;2 version&nbsp;4) be equal to the unit
 * associated with the species' quantity.  <em>Restrictions</em>: There
 * must not be both an AssignmentRule 'variable' attribute and a
 * SpeciesReference 'species' attribute having the same value in a model,
 * unless the referenced Species @if conly structure @else object@endif has
 * its 'boundaryCondition' attribute set to @c true.  In other words, an
 * assignment rule cannot be defined for a species that is created or
 * destroyed in a reaction unless that species is defined as a boundary
 * condition in the model.
 *
 * <li> (For SBML Level&nbsp;3 only) <em>In the case of a species
 * reference</em>, an assignment rule sets the stoichiometry of the
 * referenced reactant or product to the value determined by the formula in
 * 'math'.  The unit associated with the value produced by the 'math'
 * formula should be consistent with the unit 'dimensionless', because
 * reactant and product stoichiometries in reactions are dimensionless
 * quantities.
  *
 * <li> <em>In the case of a compartment</em>, an SBML assignment rule sets
 * the referenced compartment's size to the value determined by the formula
 * in the 'math' subelement of the AssignmentRule
 * @if conly structure @else object@endif.  The overall units of the
 * formula in 'math' @em should (in SBML Level&nbsp;2 Version&nbsp;4 and in
 * SBML Level&nbsp;3) or @em must (in SBML releases prior to Level&nbsp;2
 * version&nbsp;4) be the same as the units of the size of the compartment.
 *
 * <li> <em>In the case of a parameter</em>, an assignment rule sets the
 * referenced parameter's value to that determined by the formula in the
 * 'math' subelement of the AssignmentRule
 * @if conly structure @else object@endif.  The overall units of the
 * formula in the 'math' subelement @em should (in SBML Level&nbsp;2
 * Version&nbsp;4 and in SBML Level&nbsp;3) or @em must (in SBML releases
 * prior to Level&nbsp;2 version&nbsp;4) be the same as the units defined for
 * the parameter.  </ul>
 * 
 * In the context of a simulation, assignment rules are in effect at all
 * times, <em>t</em> >= <em>0</em>.  For purposes of evaluating
 * expressions that involve the <em>delay</em> 'csymbol' (see the SBML
 * Level&nbsp;2 specification), assignment rules are considered to apply
 * also at <em>t</em> <= <em>0</em>.  Please consult the relevant
 * SBML specification for additional information about the semantics of
 * assignments, rules, and entity values for simulation time <em>t</em>
 * <= <em>0</em>.
 *
 * A model must not contain more than one AssignmentRule or RateRule
 * @if conly structure @else object@endif having the same value of
 * 'variable'; in other words, in the set of all assignment rules and rate
 * rules in an SBML model, each variable appearing in the left-hand sides can
 * only appear once.  This simply follows from the fact that an indeterminate
 * system would result if a model contained more than one assignment rule for
 * the same variable or both an assignment rule and a rate rule for the same
 * variable.
 *
 * Similarly, a model must also not contain <em>both</em> an AssignmentRule
 * and an InitialAssignment definition for the same variable, because both
 * kinds of constructs apply prior to and at the start of simulation time,
 * i.e., <em>t</em> <= <em>0</em>.  If a model contained both an
 * initial assignment and an assignment rule for the same variable, an
 * indeterminate system would result.
 *
 * The value calculated by an AssignmentRule
 * @if conly structure @else object@endif overrides the value assigned to
 * the given symbol by the model component defining that symbol.  For
 * example, if a Compartment @if conly structure @else object@endif's
 * 'size' attribute value is set in its definition, and the model also
 * contains an AssignmentRule @if conly structure @else object@endif 
 * having that compartment's 'id' as its 'variable' value, then the 'size'
 * assigned in the Compartment @if conly structure @else object@endif
 * definition is ignored and the value assigned based on the computation
 * defined in the AssignmentRule.  This does <em>not</em> mean that a
 * definition for a given symbol can be omitted if there is an AssignmentRule
 * @if conly structure @else object@endif involving it.  For example, 
 * there must be a Parameter @if conly structure @else object@endif
 * definition for a given parameter if there is an AssignmentRule definition
 * for that parameter.  It is only a question of which value definition takes
 * precedence.
 *
 *
 * @section rules-general General summary of SBML rules
 *
 * In SBML Level&nbsp;3 as well as Level&nbsp;2, rules are separated into three
 * subclasses for the benefit of model analysis software.  The three
 * subclasses are based on the following three different possible functional
 * forms (where <em>x</em> is a variable, <em>f</em> is some arbitrary
 * function returning a numerical result, <b><em>V</em></b> is a vector of
 * variables that does not include <em>x</em>, and <b><em>W</em></b> is a
 * vector of variables that may include <em>x</em>):
 *
 * <table border='0' cellpadding='0' class='centered' style='font-size: small'>
 * <tr><td width='120px'><em>Algebraic:</em></td><td width='250px'>left-hand side is zero</td><td><em>0 = f(<b>W</b>)</em></td></tr>
 * <tr><td><em>Assignment:</em></td><td>left-hand side is a scalar:</td><td><em>x = f(<b>V</b>)</em></td></tr>
 * <tr><td><em>Rate:</em></td><td>left-hand side is a rate-of-change:</td><td><em>dx/dt = f(<b>W</b>)</em></td></tr>
 * </table>
 *
 * In their general form given above, there is little to distinguish
 * between <em>assignment</em> and <em>algebraic</em> rules.  They are treated as
 * separate cases for the following reasons:
 *
 * @li <em>Assignment</em> rules can simply be evaluated to calculate
 * intermediate values for use in numerical methods.  They are statements
 * of equality that hold at all times.  (For assignments that are only
 * performed once, see InitialAssignment.)

 * @li SBML needs to place restrictions on assignment rules, for example
 * the restriction that assignment rules cannot contain algebraic loops.
 *
 * @li Some simulators do not contain numerical solvers capable of solving
 * unconstrained algebraic equations, and providing more direct forms such
 * as assignment rules may enable those simulators to process models they
 * could not process if the same assignments were put in the form of
 * general algebraic equations;
 *
 * @li Those simulators that <em>can</em> solve these algebraic equations make a
 * distinction between the different categories listed above; and
 *
 * @li Some specialized numerical analyses of models may only be applicable
 * to models that do not contain <em>algebraic</em> rules.
 *
 * The approach taken to covering these cases in SBML is to define an
 * abstract Rule structure containing a subelement, 'math', to hold the
 * right-hand side expression, then to derive subtypes of Rule that add
 * attributes to distinguish the cases of algebraic, assignment and rate
 * rules.  The 'math' subelement must contain a MathML expression defining the
 * mathematical formula of the rule.  This MathML formula must return a
 * numerical value.  The formula can be an arbitrary expression referencing
 * the variables and other entities in an SBML model.
 *
 * Each of the three subclasses of Rule (AssignmentRule, AlgebraicRule,
 * RateRule) inherit the the 'math' subelement and other fields from SBase.
 * The AssignmentRule and RateRule classes add an additional attribute,
 * 'variable'.  See the definitions of AssignmentRule, AlgebraicRule and
 * RateRule for details about the structure and interpretation of each one.
 *
 * @section rules-restrictions Additional restrictions on SBML rules
 *
 * An important design goal of SBML rule semantics is to ensure that a
 * model's simulation and analysis results will not be dependent on when or
 * how often rules are evaluated.  To achieve this, SBML needs to place two
 * restrictions on rule use.  The first concerns algebraic loops in the system
 * of assignments in a model, and the second concerns overdetermined systems.
 *
 * @subsection rules-no-loops A model must not contain algebraic loops
 *
 * The combined set of InitialAssignment, AssignmentRule and KineticLaw
 * objects in a model constitute a set of assignment statements that should be
 * considered as a whole.  (A KineticLaw object is counted as an assignment
 * because it assigns a value to the symbol contained in the 'id' attribute of
 * the Reaction object in which it is defined.)  This combined set of
 * assignment statements must not contain algebraic loops---dependency
 * chains between these statements must terminate.  To put this more formally,
 * consider a directed graph in which nodes are assignment statements and
 * directed arcs exist for each occurrence of an SBML species, compartment or
 * parameter symbol in an assignment statement's 'math' subelement.  Let the
 * directed arcs point from the statement assigning the symbol to the
 * statements that contain the symbol in their 'math' subelement expressions.
 * This graph must be acyclic.
 *
 * SBML does not specify when or how often rules should be evaluated.
 * Eliminating algebraic loops ensures that assignment statements can be
 * evaluated any number of times without the result of those evaluations
 * changing.  As an example, consider the set of equations <em>x = x + 1</em>,
 * <em>y = z + 200</em> and <em>z = y + 100</em>.  If this set of equations
 * were interpreted as a set of assignment statements, it would be invalid
 * because the rule for <em>x</em> refers to <em>x</em> (exhibiting one type
 * of loop), and the rule for <em>y</em> refers to <em>z</em> while the rule
 * for <em>z</em> refers back to <em>y</em> (exhibiting another type of loop).
 * Conversely, the following set of equations would constitute a valid set of
 * assignment statements: <em>x = 10</em>, <em>y = z + 200</em>, and <em>z = x
 * + 100</em>.
 *
 * @subsection rules-not-overdetermined A model must not be overdetermined
 *
 * An SBML model must not be overdetermined; that is, a model must not
 * define more equations than there are unknowns in a model.  An SBML model
 * that does not contain AlgebraicRule structures cannot be overdetermined.
 *
 * LibSBML implements the static analysis procedure described in
 * Appendix&nbsp;B of the SBML Level&nbsp;3 Version&nbsp;1 Core
 * specification for assessing whether a model is overdetermined.
 *
 * (In summary, assessing whether a given continuous, deterministic,
 * mathematical model is overdetermined does not require dynamic analysis; it
 * can be done by analyzing the system of equations created from the model.
 * One approach is to construct a bipartite graph in which one set of vertices
 * represents the variables and the other the set of vertices represents the
 * equations.  Place edges between vertices such that variables in the system
 * are linked to the equations that determine them.  For algebraic equations,
 * there will be edges between the equation and each variable occurring in the
 * equation.  For ordinary differential equations (such as those defined by
 * rate rules or implied by the reaction rate definitions), there will be a
 * single edge between the equation and the variable determined by that
 * differential equation.  A mathematical model is overdetermined if the
 * maximal matchings of the bipartite graph contain disconnected vertexes
 * representing equations.  If one maximal matching has this property, then
 * all the maximal matchings will have this property; i.e., it is only
 * necessary to find one maximal matching.)
 *
 * @section RuleType_t Rule types for SBML Level 1
 *
 * SBML Level 1 uses a different scheme than SBML Level 2 and Level 3 for
 * distinguishing rules; specifically, it uses an attribute whose value is
 * drawn from an enumeration of 3 values.  LibSBML supports this using methods
 * that work @if clike a libSBML enumeration type,
 * @link Rule::RuleType_t RuleType_t@endlink, whose values
 * are @else with the enumeration values @endif listed below.
 *
 * @li @link libsbml#RULE_TYPE_RATE RULE_TYPE_RATE@endlink: Indicates
 * the rule is a 'rate' rule.
 * @li @link libsbml#RULE_TYPE_SCALAR RULE_TYPE_SCALAR@endlink:
 * Indicates the rule is a 'scalar' rule.
 * @li @link libsbml#RULE_TYPE_INVALID RULE_TYPE_INVALID@endlink:
 * Indicates the rule type is unknown or not yet set.
 *
 *
 */

public class AssignmentRule : Rule {
	private HandleRef swigCPtr;
	
	internal AssignmentRule(IntPtr cPtr, bool cMemoryOwn) : base(libsbmlPINVOKE.AssignmentRule_SWIGUpcast(cPtr), cMemoryOwn)
	{
		//super(libsbmlPINVOKE.AssignmentRuleUpcast(cPtr), cMemoryOwn);
		swigCPtr = new HandleRef(this, cPtr);
	}
	
	internal static HandleRef getCPtr(AssignmentRule obj)
	{
		return (obj == null) ? new HandleRef(null, IntPtr.Zero) : obj.swigCPtr;
	}
	
	internal static HandleRef getCPtrAndDisown (AssignmentRule obj)
	{
		HandleRef ptr = new HandleRef(null, IntPtr.Zero);
		
		if (obj != null)
		{
			ptr             = obj.swigCPtr;
			obj.swigCMemOwn = false;
		}
		
		return ptr;
	}

  ~AssignmentRule() {
    Dispose();
  }

  public override void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          libsbmlPINVOKE.delete_AssignmentRule(swigCPtr);
        }
        swigCPtr = new HandleRef(null, IntPtr.Zero);
      }
      GC.SuppressFinalize(this);
      base.Dispose();
    }
  }

  
/**
   * Creates a new AssignmentRule using the given SBML @p level and @p version
   * values.
   *
   * @param level a long integer, the SBML Level to assign to this AssignmentRule.
   *
   * @param version a long integer, the SBML Version to assign to this
   * AssignmentRule.
   *
   * @throws SBMLConstructorException
   * Thrown if the given @p level and @p version combination, or this kind
   * of SBML object, are either invalid or mismatched with respect to the
   * parent SBMLDocument object.
   * 
   *
 * @note Attempting to add an object to an SBMLDocument having a different
 * combination of SBML Level, Version and XML namespaces than the object
 * itself will result in an error at the time a caller attempts to make the
 * addition.  A parent object must have compatible Level, Version and XML
 * namespaces.  (Strictly speaking, a parent may also have more XML
 * namespaces than a child, but the reverse is not permitted.)  The
 * restriction is necessary to ensure that an SBML model has a consistent
 * overall structure.  This requires callers to manage their objects
 * carefully, but the benefit is increased flexibility in how models can be
 * created by permitting callers to create objects bottom-up if desired.  In
 * situations where objects are not yet attached to parents (e.g.,
 * SBMLDocument), knowledge of the intented SBML Level and Version help
 * libSBML determine such things as whether it is valid to assign a
 * particular value to an attribute.
 *
 *
   */ public
 AssignmentRule(long level, long version) : this(libsbmlPINVOKE.new_AssignmentRule__SWIG_0(level, version), true) {
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  
/**
   * Creates a new AssignmentRule using the given SBMLNamespaces object
   * @p sbmlns.
   *
   *
 * 
 * The SBMLNamespaces object encapsulates SBML Level/Version/namespaces
 * information.  It is used to communicate the SBML Level, Version, and (in
 * Level&nbsp;3) packages used in addition to SBML Level&nbsp;3 Core.  A
 * common approach to using libSBML's SBMLNamespaces facilities is to create an
 * SBMLNamespaces object somewhere in a program once, then hand that object
 * as needed to object constructors that accept SBMLNamespaces as arguments.
 *
 *
   *
   * @param sbmlns an SBMLNamespaces object.
   *
   * @throws SBMLConstructorException
   * Thrown if the given @p level and @p version combination, or this kind
   * of SBML object, are either invalid or mismatched with respect to the
   * parent SBMLDocument object.
   *
   *
 * @note Attempting to add an object to an SBMLDocument having a different
 * combination of SBML Level, Version and XML namespaces than the object
 * itself will result in an error at the time a caller attempts to make the
 * addition.  A parent object must have compatible Level, Version and XML
 * namespaces.  (Strictly speaking, a parent may also have more XML
 * namespaces than a child, but the reverse is not permitted.)  The
 * restriction is necessary to ensure that an SBML model has a consistent
 * overall structure.  This requires callers to manage their objects
 * carefully, but the benefit is increased flexibility in how models can be
 * created by permitting callers to create objects bottom-up if desired.  In
 * situations where objects are not yet attached to parents (e.g.,
 * SBMLDocument), knowledge of the intented SBML Level and Version help
 * libSBML determine such things as whether it is valid to assign a
 * particular value to an attribute.
 *
 *
   */ public
 AssignmentRule(SBMLNamespaces sbmlns) : this(libsbmlPINVOKE.new_AssignmentRule__SWIG_1(SBMLNamespaces.getCPtr(sbmlns)), true) {
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  
/**
   * Creates and returns a deep copy of this AssignmentRule object.
   *
   * @return the (deep) copy of this Rule object.
   */ public new
 AssignmentRule clone() {
    IntPtr cPtr = libsbmlPINVOKE.AssignmentRule_clone(swigCPtr);
    AssignmentRule ret = (cPtr == IntPtr.Zero) ? null : new AssignmentRule(cPtr, true);
    return ret;
  }

  
/**
   * Predicate returning @c true if all the required attributes for this
   * AssignmentRule object have been set.
   *
   * In SBML Levels&nbsp;2&ndash;3, the only required attribute for
   * an AssignmentRule object is 'variable'.  For Level&nbsp;1, where the
   * equivalent attribute is known by different names ('compartment',
   * 'species', or 'name', depending on the type of object), there is an
   * additional required attribute called 'formula'.
   *
   * @return @c true if the required attributes have been set, @c false
   * otherwise.
   */ public new
 bool hasRequiredAttributes() {
    bool ret = libsbmlPINVOKE.AssignmentRule_hasRequiredAttributes(swigCPtr);
    return ret;
  }

  
/**
   *
 * Replaces all uses of a given @c SIdRef type attribute value with another
 * value.
 *
 *
 * 

 * In SBML, object identifiers are of a data type called <code>SId</code>.
 * In SBML Level&nbsp;3, an explicit data type called <code>SIdRef</code> was
 * introduced for attribute values that refer to <code>SId</code> values; in
 * previous Levels of SBML, this data type did not exist and attributes were
 * simply described to as 'referring to an identifier', but the effective
 * data type was the same as <code>SIdRef</code>in Level&nbsp;3.  These and
 * other methods of libSBML refer to the type <code>SIdRef</code> for all
 * Levels of SBML, even if the corresponding SBML specification did not
 * explicitly name the data type.
 *
 *
 *
 * This method works by looking at all attributes and (if appropriate)
 * mathematical formulas in MathML content, comparing the referenced
 * identifiers to the value of @p oldid.  If any matches are found, the
 * matching values are replaced with @p newid.  The method does @em not
 * descend into child elements.
 *
 * @param oldid the old identifier
 * @param newid the new identifier
 *
 *
   */ public new
 void renameSIdRefs(string oldid, string newid) {
    libsbmlPINVOKE.AssignmentRule_renameSIdRefs(swigCPtr, oldid, newid);
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

}

}
