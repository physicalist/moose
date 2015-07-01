/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.4
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.sbml.libsbml;

/** 
 *  Interface to an XML output stream.
 <p>
 * <p style='color: #777; font-style: italic'>
This class of objects is defined by libSBML only and has no direct
equivalent in terms of SBML components.  This class is not prescribed by
the SBML specifications, although it is used to implement features
defined in SBML.
</p>

 <p>
 * SBML content is serialized using XML; the resulting data can be stored and
 * read to/from a file or data stream.  Low-level XML parsers such as Xerces
 * provide facilities to read XML data.  To permit the use of different XML
 * parsers (Xerces, Expat or libxml2), libSBML implements an abstraction
 * layer.  {@link XMLInputStream} and {@link XMLOutputStream} are two parts of that
 * abstraction layer.
 <p>
 * {@link XMLOutputStream} provides a wrapper above output streams to facilitate
 * writing XML.  {@link XMLOutputStream} keeps track of start and end elements,
 * indentation, XML namespace prefixes, and more.  The interface provides
 * features for converting non-text data types into appropriate textual form;
 * this takes the form of overloaded <code>writeAttribute(...)</code> methods
 * that allow users to simply use the same method with any data type.  For
 * example, suppose an element <code>testElement</code> has two attributes, <code>size</code> and
 * <code>id</code>, and the attributes are variables in your code as follows:
<p>
<pre class='fragment'>
double size = 3.2;
String id = 'id';
</pre>
<p>
  * Then, the element and the attributes can be written to the
  * standard output stream (provided as <code>cout</code> in the libSBML
  * language bindings) as follows:
<p>
<pre class='fragment'>
import org.sbml.libsbml.XMLOutputStream;
import org.sbml.libsbml.libsbml;

public class test
{
    public static void main (String[] args)
    {
        double size = 3.2;
        String id = 'id';

        // Create an {@link XMLOutputStream} object that will write to the
        // standard output stream, which is provide in libSBML's
        // Java language interface as the object 'libsbml.cout'.

        {@link XMLOutputStream} xos = new {@link XMLOutputStream}(libsbml.cout);

        // Create the start element, write the attributes, and close
        // the element.  The output will be written immediately as
        // each method is called.

        xos.startElement('testElement');
        xos.writeAttribute('size', size);
        xos.writeAttribute('id', id);
        xos.endElement('testElement');
    }

    static
    {
        System.loadLibrary('sbmlj');
    }
}
</pre>
<p>
 * Other classes in SBML take {@link XMLOutputStream} objects as arguments, and use
 * that to write elements and attributes seamlessly to the XML output stream.
 <p>
 * It is also worth noting that unlike {@link XMLInputStream}, {@link XMLOutputStream} is
 * actually independent of the underlying XML parsers.  It does not use the
 * XML parser libraries at all.
 <p>
 * @note The convenience of the {@link XMLInputStream} and {@link XMLOutputStream}
 * abstraction may be useful for developers interested in creating parsers
 * for other XML formats besides SBML.  It can provide developers with a
 * layer above more basic XML parsers, as well as some useful programmatic
 * elements such as {@link XMLToken}, {@link XMLError}, etc.
 <p>
 * @see XMLInputStream
 */

public class XMLOutputStream {
   private long swigCPtr;
   protected boolean swigCMemOwn;

   protected XMLOutputStream(long cPtr, boolean cMemoryOwn)
   {
     swigCMemOwn = cMemoryOwn;
     swigCPtr    = cPtr;
   }

   protected static long getCPtr(XMLOutputStream obj)
   {
     return (obj == null) ? 0 : obj.swigCPtr;
   }

   protected static long getCPtrAndDisown (XMLOutputStream obj)
   {
     long ptr = 0;

     if (obj != null)
     {
       ptr             = obj.swigCPtr;
       obj.swigCMemOwn = false;
     }

     return ptr;
   }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        libsbmlJNI.delete_XMLOutputStream(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  /**
   * Equality comparison method for XMLOutputStream.
   * <p>
   * Because the Java methods for libSBML are actually wrappers around code
   * implemented in C++ and C, certain operations will not behave as
   * expected.  Equality comparison is one such case.  An instance of a
   * libSBML object class is actually a <em>proxy object</em>
   * wrapping the real underlying C/C++ object.  The normal <code>==</code>
   * equality operator in Java will <em>only compare the Java proxy objects</em>,
   * not the underlying native object.  The result is almost never what you
   * want in practical situations.  Unfortunately, Java does not provide a
   * way to override <code>==</code>.
   *  <p>
   * The alternative that must be followed is to use the
   * <code>equals()</code> method.  The <code>equals</code> method on this
   * class overrides the default java.lang.Object one, and performs an
   * intelligent comparison of instances of objects of this class.  The
   * result is an assessment of whether two libSBML Java objects are truly 
   * the same underlying native-code objects.
   *  <p>
   * The use of this method in practice is the same as the use of any other
   * Java <code>equals</code> method.  For example,
   * <em>a</em><code>.equals(</code><em>b</em><code>)</code> returns
   * <code>true</code> if <em>a</em> and <em>b</em> are references to the
   * same underlying object.
   *
   * @param sb a reference to an object to which the current object
   * instance will be compared
   *
   * @return <code>true</code> if <code>sb</code> refers to the same underlying 
   * native object as this one, <code>false</code> otherwise
   */
  public boolean equals(Object sb)
  {
    if ( this == sb ) 
    {
      return true;
    }
    return swigCPtr == getCPtr((XMLOutputStream)(sb));
  }

  /**
   * Returns a hashcode for this XMLOutputStream object.
   *
   * @return a hash code usable by Java methods that need them.
   */
  public int hashCode()
  {
    return (int)(swigCPtr^(swigCPtr>>>32));
  }

  
/**
   * Creates a new {@link XMLOutputStream} that wraps the given <code>stream</code>.
   <p>
   * <p>
 * The functionality associated with the <code>programName</code> and 
 * <code>programVersion</code> arguments concerns an optional comment that libSBML can
 * write at the beginning of the output stream.  The comment is intended
 * for human readers of the XML file, and has the following form:
 * <pre class='fragment'>
&lt;!-- Created by &lt;program name&gt; version &lt;program version&gt;
on yyyy-MM-dd HH:mm with libSBML version &lt;libsbml version&gt;. --&gt;
</pre>
 <p>
 * This program information comment is a separate item from the XML
 * declaration that this method can also write to this output stream.  The
 * comment is also not mandated by any SBML specification.  This libSBML
 * functionality is provided for the convenience of calling programs, and to
 * help humans trace the origin of SBML files.
   <p>
   * <p>
 * The XML declaration has the form
 * <pre class='fragment'>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
</pre>
 * Note that the SBML specifications require the use of UTF-8 encoding and
 * version 1.0, so for SBML documents, the above is the standard XML
 * declaration.
   <p>
   * @param stream the input stream to wrap.
   <p>
   * @param encoding the XML encoding to declare in the output. This value
   * should be <code>'UTF-8'</code> for SBML documents.  The default value
   * is <code>'UTF-8'</code> if no value is supplied for this parameter.
   <p>
   * @param writeXMLDecl whether to write a standard XML declaration at
   * the beginning of the content written on <code>stream</code>.  The default is
   * <code>true.</code>
   <p>
   * @param programName an optional program name to write as a comment
   * in the output stream.
   <p>
   * @param programVersion an optional version identification string to write
   * as a comment in the output stream.
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 XMLOutputStream(OStream stream, String encoding, boolean writeXMLDecl, String programName, String programVersion) throws org.sbml.libsbml.XMLConstructorException {
    this(libsbmlJNI.new_XMLOutputStream__SWIG_0(SWIGTYPE_p_std__ostream.getCPtr(stream.get_ostream()), stream, encoding, writeXMLDecl, programName, programVersion), true);
  }

  
/**
   * Creates a new {@link XMLOutputStream} that wraps the given <code>stream</code>.
   <p>
   * <p>
 * The functionality associated with the <code>programName</code> and 
 * <code>programVersion</code> arguments concerns an optional comment that libSBML can
 * write at the beginning of the output stream.  The comment is intended
 * for human readers of the XML file, and has the following form:
 * <pre class='fragment'>
&lt;!-- Created by &lt;program name&gt; version &lt;program version&gt;
on yyyy-MM-dd HH:mm with libSBML version &lt;libsbml version&gt;. --&gt;
</pre>
 <p>
 * This program information comment is a separate item from the XML
 * declaration that this method can also write to this output stream.  The
 * comment is also not mandated by any SBML specification.  This libSBML
 * functionality is provided for the convenience of calling programs, and to
 * help humans trace the origin of SBML files.
   <p>
   * <p>
 * The XML declaration has the form
 * <pre class='fragment'>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
</pre>
 * Note that the SBML specifications require the use of UTF-8 encoding and
 * version 1.0, so for SBML documents, the above is the standard XML
 * declaration.
   <p>
   * @param stream the input stream to wrap.
   <p>
   * @param encoding the XML encoding to declare in the output. This value
   * should be <code>'UTF-8'</code> for SBML documents.  The default value
   * is <code>'UTF-8'</code> if no value is supplied for this parameter.
   <p>
   * @param writeXMLDecl whether to write a standard XML declaration at
   * the beginning of the content written on <code>stream</code>.  The default is
   * <code>true.</code>
   <p>
   * @param programName an optional program name to write as a comment
   * in the output stream.
   <p>
   * @param programVersion an optional version identification string to write
   * as a comment in the output stream.
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 XMLOutputStream(OStream stream, String encoding, boolean writeXMLDecl, String programName) throws org.sbml.libsbml.XMLConstructorException {
    this(libsbmlJNI.new_XMLOutputStream__SWIG_1(SWIGTYPE_p_std__ostream.getCPtr(stream.get_ostream()), stream, encoding, writeXMLDecl, programName), true);
  }

  
/**
   * Creates a new {@link XMLOutputStream} that wraps the given <code>stream</code>.
   <p>
   * <p>
 * The functionality associated with the <code>programName</code> and 
 * <code>programVersion</code> arguments concerns an optional comment that libSBML can
 * write at the beginning of the output stream.  The comment is intended
 * for human readers of the XML file, and has the following form:
 * <pre class='fragment'>
&lt;!-- Created by &lt;program name&gt; version &lt;program version&gt;
on yyyy-MM-dd HH:mm with libSBML version &lt;libsbml version&gt;. --&gt;
</pre>
 <p>
 * This program information comment is a separate item from the XML
 * declaration that this method can also write to this output stream.  The
 * comment is also not mandated by any SBML specification.  This libSBML
 * functionality is provided for the convenience of calling programs, and to
 * help humans trace the origin of SBML files.
   <p>
   * <p>
 * The XML declaration has the form
 * <pre class='fragment'>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
</pre>
 * Note that the SBML specifications require the use of UTF-8 encoding and
 * version 1.0, so for SBML documents, the above is the standard XML
 * declaration.
   <p>
   * @param stream the input stream to wrap.
   <p>
   * @param encoding the XML encoding to declare in the output. This value
   * should be <code>'UTF-8'</code> for SBML documents.  The default value
   * is <code>'UTF-8'</code> if no value is supplied for this parameter.
   <p>
   * @param writeXMLDecl whether to write a standard XML declaration at
   * the beginning of the content written on <code>stream</code>.  The default is
   * <code>true.</code>
   <p>
   * @param programName an optional program name to write as a comment
   * in the output stream.
   <p>
   * @param programVersion an optional version identification string to write
   * as a comment in the output stream.
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 XMLOutputStream(OStream stream, String encoding, boolean writeXMLDecl) throws org.sbml.libsbml.XMLConstructorException {
    this(libsbmlJNI.new_XMLOutputStream__SWIG_2(SWIGTYPE_p_std__ostream.getCPtr(stream.get_ostream()), stream, encoding, writeXMLDecl), true);
  }

  
/**
   * Creates a new {@link XMLOutputStream} that wraps the given <code>stream</code>.
   <p>
   * <p>
 * The functionality associated with the <code>programName</code> and 
 * <code>programVersion</code> arguments concerns an optional comment that libSBML can
 * write at the beginning of the output stream.  The comment is intended
 * for human readers of the XML file, and has the following form:
 * <pre class='fragment'>
&lt;!-- Created by &lt;program name&gt; version &lt;program version&gt;
on yyyy-MM-dd HH:mm with libSBML version &lt;libsbml version&gt;. --&gt;
</pre>
 <p>
 * This program information comment is a separate item from the XML
 * declaration that this method can also write to this output stream.  The
 * comment is also not mandated by any SBML specification.  This libSBML
 * functionality is provided for the convenience of calling programs, and to
 * help humans trace the origin of SBML files.
   <p>
   * <p>
 * The XML declaration has the form
 * <pre class='fragment'>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
</pre>
 * Note that the SBML specifications require the use of UTF-8 encoding and
 * version 1.0, so for SBML documents, the above is the standard XML
 * declaration.
   <p>
   * @param stream the input stream to wrap.
   <p>
   * @param encoding the XML encoding to declare in the output. This value
   * should be <code>'UTF-8'</code> for SBML documents.  The default value
   * is <code>'UTF-8'</code> if no value is supplied for this parameter.
   <p>
   * @param writeXMLDecl whether to write a standard XML declaration at
   * the beginning of the content written on <code>stream</code>.  The default is
   * <code>true.</code>
   <p>
   * @param programName an optional program name to write as a comment
   * in the output stream.
   <p>
   * @param programVersion an optional version identification string to write
   * as a comment in the output stream.
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 XMLOutputStream(OStream stream, String encoding) throws org.sbml.libsbml.XMLConstructorException {
    this(libsbmlJNI.new_XMLOutputStream__SWIG_3(SWIGTYPE_p_std__ostream.getCPtr(stream.get_ostream()), stream, encoding), true);
  }

  
/**
   * Creates a new {@link XMLOutputStream} that wraps the given <code>stream</code>.
   <p>
   * <p>
 * The functionality associated with the <code>programName</code> and 
 * <code>programVersion</code> arguments concerns an optional comment that libSBML can
 * write at the beginning of the output stream.  The comment is intended
 * for human readers of the XML file, and has the following form:
 * <pre class='fragment'>
&lt;!-- Created by &lt;program name&gt; version &lt;program version&gt;
on yyyy-MM-dd HH:mm with libSBML version &lt;libsbml version&gt;. --&gt;
</pre>
 <p>
 * This program information comment is a separate item from the XML
 * declaration that this method can also write to this output stream.  The
 * comment is also not mandated by any SBML specification.  This libSBML
 * functionality is provided for the convenience of calling programs, and to
 * help humans trace the origin of SBML files.
   <p>
   * <p>
 * The XML declaration has the form
 * <pre class='fragment'>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
</pre>
 * Note that the SBML specifications require the use of UTF-8 encoding and
 * version 1.0, so for SBML documents, the above is the standard XML
 * declaration.
   <p>
   * @param stream the input stream to wrap.
   <p>
   * @param encoding the XML encoding to declare in the output. This value
   * should be <code>'UTF-8'</code> for SBML documents.  The default value
   * is <code>'UTF-8'</code> if no value is supplied for this parameter.
   <p>
   * @param writeXMLDecl whether to write a standard XML declaration at
   * the beginning of the content written on <code>stream</code>.  The default is
   * <code>true.</code>
   <p>
   * @param programName an optional program name to write as a comment
   * in the output stream.
   <p>
   * @param programVersion an optional version identification string to write
   * as a comment in the output stream.
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 XMLOutputStream(OStream stream) throws org.sbml.libsbml.XMLConstructorException {
    this(libsbmlJNI.new_XMLOutputStream__SWIG_4(SWIGTYPE_p_std__ostream.getCPtr(stream.get_ostream()), stream), true);
  }

  
/**
   * Writes the given XML end element name to this {@link XMLOutputStream}.
   <p>
   * @param name the name of the element.
   <p>
   * @param prefix an optional XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 void endElement(String name, String prefix) {
    libsbmlJNI.XMLOutputStream_endElement__SWIG_0(swigCPtr, this, name, prefix);
  }

  
/**
   * Writes the given XML end element name to this {@link XMLOutputStream}.
   <p>
   * @param name the name of the element.
   <p>
   * @param prefix an optional XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 void endElement(String name) {
    libsbmlJNI.XMLOutputStream_endElement__SWIG_1(swigCPtr, this, name);
  }

  
/**
   * Writes the given element to the stream.
   <p>
   * @param triple the XML element to write.
   */ public
 void endElement(XMLTriple triple) {
    libsbmlJNI.XMLOutputStream_endElement__SWIG_2(swigCPtr, this, XMLTriple.getCPtr(triple), triple);
  }

  
/**
   * Turns automatic indentation on or off for this {@link XMLOutputStream}.
   <p>
   * @param indent if <code>true</code>, automatic indentation is turned on.
   */ public
 void setAutoIndent(boolean indent) {
    libsbmlJNI.XMLOutputStream_setAutoIndent(swigCPtr, this, indent);
  }

  
/**
   * Writes the given XML start element name to this {@link XMLOutputStream}.
   <p>
   * @param name the name of the element.
   <p>
   * @param prefix an optional XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 void startElement(String name, String prefix) {
    libsbmlJNI.XMLOutputStream_startElement__SWIG_0(swigCPtr, this, name, prefix);
  }

  
/**
   * Writes the given XML start element name to this {@link XMLOutputStream}.
   <p>
   * @param name the name of the element.
   <p>
   * @param prefix an optional XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 void startElement(String name) {
    libsbmlJNI.XMLOutputStream_startElement__SWIG_1(swigCPtr, this, name);
  }

  
/**
   * Writes the given XML start element
   * <code><em>prefix</em>:<em>name</em></code> on this output stream.
   <p>
   * @param triple the start element to write.
   */ public
 void startElement(XMLTriple triple) {
    libsbmlJNI.XMLOutputStream_startElement__SWIG_2(swigCPtr, this, XMLTriple.getCPtr(triple), triple);
  }

  
/**
   * Writes the given XML start and end element name to this {@link XMLOutputStream}.
   <p>
   * @param name the name of the element.
   <p>
   * @param prefix an optional XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 void startEndElement(String name, String prefix) {
    libsbmlJNI.XMLOutputStream_startEndElement__SWIG_0(swigCPtr, this, name, prefix);
  }

  
/**
   * Writes the given XML start and end element name to this {@link XMLOutputStream}.
   <p>
   * @param name the name of the element.
   <p>
   * @param prefix an optional XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)
   <p>
   * 
</dl><dl class="docnote"><dt><b>Documentation note:</b></dt><dd>
The native C++ implementation of this method defines a default argument
value. In the documentation generated for different libSBML language
bindings, you may or may not see corresponding arguments in the method
declarations. For example, in Java and C#, a default argument is handled by
declaring two separate methods, with one of them having the argument and
the other one lacking the argument. However, the libSBML documentation will
be <em>identical</em> for both methods. Consequently, if you are reading
this and do not see an argument even though one is described, please look
for descriptions of other variants of this method near where this one
appears in the documentation.
</dd></dl>
 
   */ public
 void startEndElement(String name) {
    libsbmlJNI.XMLOutputStream_startEndElement__SWIG_1(swigCPtr, this, name);
  }

  
/**
   * Writes the given start element to this output stream.
   <p>
   * @param triple the XML element to write.
   */ public
 void startEndElement(XMLTriple triple) {
    libsbmlJNI.XMLOutputStream_startEndElement__SWIG_2(swigCPtr, this, XMLTriple.getCPtr(triple), triple);
  }

  
/**
   * Writes the given attribute and value to this output stream.
   <p>
   * @param name the name of the attribute.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(String name, String value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_0(swigCPtr, this, name, value);
  }

  
/**
   * Writes the given namespace-prefixed attribute value to this output stream.
   <p>
   * @param name the name of the attribute.
   <p>
   * @param prefix an XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)  See other versions of
   * this method for a variant that does not require a prefix.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(String name, String prefix, String value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_1(swigCPtr, this, name, prefix, value);
  }

  
/**
   * Writes the given attribute and value to this output stream.
   <p>
   * @param triple the attribute, in the form of an {@link XMLTriple}.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(XMLTriple triple, String value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_2(swigCPtr, this, XMLTriple.getCPtr(triple), triple, value);
  }

  
/**
   * Writes the given attribute and value to this output stream.
   <p>
   * @param name the name of the attribute.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(String name, boolean value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_6(swigCPtr, this, name, value);
  }

  
/**
   * Writes the given namespace-prefixed attribute value to this output stream.
   <p>
   * @param name the name of the attribute.
   <p>
   * @param prefix an XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)  See other versions of
   * this method for a variant that does not require a prefix.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(String name, String prefix, boolean value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_7(swigCPtr, this, name, prefix, value);
  }

  
/**
   * Writes the given attribute and value to this output stream.
   <p>
   * @param triple the attribute, in the form of an {@link XMLTriple}.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(XMLTriple triple, boolean value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_8(swigCPtr, this, XMLTriple.getCPtr(triple), triple, value);
  }

  
/**
   * Writes the given attribute and value to this output stream.
   <p>
   * @param name the name of the attribute.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(String name, double value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_9(swigCPtr, this, name, value);
  }

  
/**
   * Writes the given namespace-prefixed attribute value to this output stream.
   <p>
   * @param name the name of the attribute.
   <p>
   * @param prefix an XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)  See other versions of
   * this method for a variant that does not require a prefix.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(String name, String prefix, double value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_10(swigCPtr, this, name, prefix, value);
  }

  
/**
   * Writes the given attribute and value to this output stream.
   <p>
   * @param triple the attribute, in the form of an {@link XMLTriple}.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(XMLTriple triple, double value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_11(swigCPtr, this, XMLTriple.getCPtr(triple), triple, value);
  }

  
/**
   * Writes the given attribute and value to this output stream.
   <p>
   * @param name the name of the attribute.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(String name, int value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_12(swigCPtr, this, name, value);
  }

  
/**
   * Writes the given namespace-prefixed attribute value to this output stream.
   <p>
   * @param name the name of the attribute.
   <p>
   * @param prefix an XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)  See other versions of
   * this method for a variant that does not require a prefix.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(String name, String prefix, int value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_13(swigCPtr, this, name, prefix, value);
  }

  
/**
   * Writes the given attribute and value to this output stream.
   <p>
   * @param triple the attribute, in the form of an {@link XMLTriple}.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(XMLTriple triple, int value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_14(swigCPtr, this, XMLTriple.getCPtr(triple), triple, value);
  }

  
/**
   * Writes the given namespace-prefixed attribute value to this output stream.
   <p>
   * @param name the name of the attribute.
   <p>
   * @param prefix an XML namespace prefix to write in front of the
   * <code>element</code> name.  (The result has the form
   * <code><em>prefix</em>:<em>name</em></code>.)  See other versions of
   * this method for a variant that does not require a prefix.
   <p>
   * @param value the value of the attribute.
   */ public
 void writeAttribute(String name, String prefix, long value) {
    libsbmlJNI.XMLOutputStream_writeAttribute__SWIG_18(swigCPtr, this, name, prefix, value);
  }

  
/**
   * Writes a standard XML declaration to this output stream.
   <p>
   * <p>
 * The XML declaration has the form
 * <pre class='fragment'>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
</pre>
 * Note that the SBML specifications require the use of UTF-8 encoding and
 * version 1.0, so for SBML documents, the above is the standard XML
 * declaration.
   */ public
 void writeXMLDecl() {
    libsbmlJNI.XMLOutputStream_writeXMLDecl(swigCPtr, this);
  }

  
/**
   * Writes an XML comment with the name and version of this program.
   <p>
   * The XML comment has the following form:
   * <pre class='fragment'>
&lt;!-- Created by &lt;program name&gt; version &lt;program version&gt;
on yyyy-MM-dd HH:mm with libSBML version &lt;libsbml version&gt;. --&gt;
</pre>
   <p>
   * See the class constructor for more information about this program
   * comment.
   <p>
   * @param programName an optional program name to write as a comment
   * in the output stream.
   <p>
   * @param programVersion an optional version identification string to write
   * as a comment in the output stream.
   */ public
 void writeComment(String programName, String programVersion) {
    libsbmlJNI.XMLOutputStream_writeComment(swigCPtr, this, programName, programVersion);
  }

  
/**
   * Decreases the indentation level for this {@link XMLOutputStream}.
   <p>
   * <p>
 * LibSBML tries to produce human-readable XML output by automatically
 * indenting the bodies of elements.  Callers can manually control
 * indentation further by using the {@link XMLOutputStream#upIndent()}
 * and {@link XMLOutputStream#downIndent()} methods to increase and
 * decrease, respectively, the current level of indentation in the
 * XML output.
   <p>
   * @see #upIndent()
   */ public
 void downIndent() {
    libsbmlJNI.XMLOutputStream_downIndent(swigCPtr, this);
  }

  
/**
   * Increases the indentation level for this {@link XMLOutputStream}.
   <p>
   * <p>
 * LibSBML tries to produce human-readable XML output by automatically
 * indenting the bodies of elements.  Callers can manually control
 * indentation further by using the {@link XMLOutputStream#upIndent()}
 * and {@link XMLOutputStream#downIndent()} methods to increase and
 * decrease, respectively, the current level of indentation in the
 * XML output.
   <p>
   * @see #downIndent()
   */ public
 void upIndent() {
    libsbmlJNI.XMLOutputStream_upIndent(swigCPtr, this);
  }

  
/**
   * Returns the {@link SBMLNamespaces} object attached to this output stream.
   <p>
   * @return the {@link SBMLNamespaces} object, or <code>null</code> if none has been set.
   */ public
 SBMLNamespaces getSBMLNamespaces() {
  return libsbml.DowncastSBMLNamespaces(libsbmlJNI.XMLOutputStream_getSBMLNamespaces(swigCPtr, this), false);
}

  
/**
   * Sets the {@link SBMLNamespaces} object associated with this output stream.
   <p>
   * @param sbmlns the namespace object.
   */ public
 void setSBMLNamespaces(SBMLNamespaces sbmlns) {
    libsbmlJNI.XMLOutputStream_setSBMLNamespaces(swigCPtr, this, SBMLNamespaces.getCPtr(sbmlns), sbmlns);
  }

}
