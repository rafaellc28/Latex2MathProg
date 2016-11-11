var mathProgEditor = null;
var simpleEditor = null;

CodeMirror.defineSimpleMode("mathprog", {
  // The start state contains the rules that are intially used
  start: [
    // The regex matches the token, the token property contains the type
    {regex: /"(?:[^\\]|\\.)*?(?:"|$)/, token: "string"},
    // Rules are matched in the order in which they appear, so there is
    // no ambiguity between this one and the one above
    {regex: /(?:param|var|maximize|minimize|s.t.|data|end|set|table|subject|to|subj|solve|check|display|forall|for|exists)\b/,
     token: "keyword"},
    {regex: /dimen|default|integer|binary|logical|symbolic|OUT|IN|and|by|cross|diff|div|else|if|in|Infinity|inter|less|mod|not|or|symdiff|then|union|within/, token: "atom"},
    {regex: /sum|prod|min|max/, token: "def"},
    {regex: /printf/, token: "builtin"},
    {regex: /abs|atan|card|ceil|cos|exp|floor|gmtime|length|log|log10|max|min|round|sin|sqrt|str2time|trunc|Irand224|Uniform01|Uniform|Normal01|Normal/, token: "def"},
    // A next property will cause the mode to move to a different state
    {regex: /#.*/, token: "comment"},
	  {regex: /\/\*/, token: "comment", next: "comment"},
    {regex: /[-+\/*=<>!]+/, token: "operator"},
    // indent and dedent properties guide autoindentation
    {regex: /[\{\[\(]/, indent: true},
    {regex: /[\}\]\)]/, dedent: true},
    {regex: /[a-zA-Z][a-zA-Z0-9]*/, token: "variable"},
    {regex: /0x[a-f\d]+|[-+]?(?:\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/i, token: "number"}
  ],
  // The multi-line comment state.
  comment: [
    {regex: /.*?\*\//, token: "comment", next: "start"},
    {regex: /.*/, token: "comment"}
  ],
  // The meta property contains global information about the mode. It
  // can contain properties like lineComment, which are supported by
  // all modes, and also directives like dontIndentStates, which are
  // specific to simple modes.
  meta: {
    dontIndentStates: ["comment"]
  }
});

CodeMirror.defineSimpleMode("latex", {
  // The start state contains the rules that are intially used
  start: [
    // The regex matches the token, the token property contains the type
    {regex: /"(?:[^\\]|\\.)*?(?:"|$)/, token: "string"},
    // Rules are matched in the order in which they appear, so there is
    // no ambiguity between this one and the one above
    {regex: /\\cdots|\\ldots|\\dots|\.\.\./, token: "atom"},
    {regex: /\+|-|\*|\\cdot|\\ast|\\div|\//, token: "operator"},
    {regex: /\|\||or|&&|and|!|not/, token: "atom"},
    {regex: /\\forall|for|\\exists/, token: "keyword"},
    {regex: /\\mathbb{Z}|\\mathbb{B}|\{0\s*,1\}|\\\{0\s*,1\\\}|\\mathbb{R}\^{\+}|\\mathbb{R}|\\mathbb{N}|\\subseteq|\\subset|\\not\\subseteq|\\not\\subset/, token: "atom"},
    {regex: /\\text\{maximize\}|\\text\{max\}|\\max|maximize|max|\\text\{maximize:\}|\\text\{max:\}|\\max:|maximize:|max:/, token: "keyword"},
    {regex: /\\text\{minimize\}|\\text\{min\}|\\min|minimize|min|\\text\{minimize:\}|\\text\{min:\}|\\min:|minimize:|min:/, token: "keyword"},
    {regex: /\\text\{subject\sto\}|\\text\{subj\.to\}|\\text\{s\.t\.\}|subject\sto|subj\.to| s\.t\.|\\text\{subject\sto:\}|\\text\{subj\.to:\}|\\text\{s\.t\.:\}|subject\sto:|subj\.to:| s\.t\.:/, token: "keyword"},
    {regex: /=|\\neq|\\leq|<|\\geq|>|%/, token: "operator"},
    {regex: /\\in|\\notin/, token: "atom"},
    {regex: /\\sum|\\prod|\\max|\\min|\\lfloor|\\rfloor|\\lceil|\\rceil|\\sin|\\cos|\\arctan|\\sqrt|\\log|\\ln|\\exp|\\vert|\|/, token: "def"},
    {regex: /\\limits|\\begin\{[a-zA-Z][a-zA-Z0-9]*[\*]?\}[\{\[][a-zA-Z0-9][a-zA-Z0-9]*[\*]?[\}\]]|\\begin\{[a-zA-Z][a-zA-Z0-9]*[\*]?\}/, token: "def"},
    {regex: /\\end\{[a-zA-Z][a-zA-Z0-9]*[\*]?\}[\{\[][a-zA-Z0-9][a-zA-Z0-9]*[\*]?[\}\]]|\\end\{[a-zA-Z][a-zA-Z0-9]*[\*]?\}/, token: "def"},
    {regex: /\\begin\{equation\}|\\end\{equation\}|\\begin\{split\}|\\end\{split\}|\\displaystyle|\\quad|\\mathclap|\\text/, token: "def"},
    {regex: /\\setminus|\\triangle|\\ominus|\\cup|\\cap|\\times|\\wedge/, token: "atom"},
    {regex: /[a-zA-Z][a-zA-Z0-9]*/, token: "variable"},
    {regex: /0x[a-f\d]+|[-+]?(?:\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/i, token: "number"}
  ],
  // The multi-line comment state.
  comment: [
    {regex: /.*?\*\//, token: "comment", next: "start"},
    {regex: /.*/, token: "comment"}
  ],
  // The meta property contains global information about the mode. It
  // can contain properties like lineComment, which are supported by
  // all modes, and also directives like dontIndentStates, which are
  // specific to simple modes.
  meta: {
    dontIndentStates: ["comment"]
  }
});

window.initMathProgEditor = function() {
	mathProgEditor = CodeMirror.fromTextArea(document.getElementById("editor"), {
	    lineNumbers: true,
	    lineWrapping: true,
	    mode: 'mathprog'
	});
	mathProgEditor.markClean();
}

window.updateMathProgEditor = function(data) {
	mathProgEditor.markClean();
	mathProgEditor.setValue(data);
	mathProgEditor.markClean();
}

window.getValueMathProgEditor = function() {
  return mathProgEditor.getValue();
}

window.setCursorMathProgEditor = function(err_line) {
  mathProgEditor.setCursor(err_line,0);
  mathProgEditor.scrollIntoView(null);
}

window.initSimpleEditor = function() {
  simpleEditor = CodeMirror.fromTextArea(document.getElementById("simpleEditor"), {
      lineNumbers: true,
      lineWrapping: true,
      mode: 'latex'
  });
  simpleEditor.markClean();
  simpleEditor.on("change", function(inst, obj) {
    PreviewSimpleEditor.Update();
  })
}

window.updateSimpleEditor = function(data) {
  simpleEditor.markClean();
  simpleEditor.setValue(data);
  simpleEditor.markClean();
}

window.getValueSimpleEditor = function() {
  return simpleEditor.getValue();
}

window.setCursorSimpleEditor = function(err_line) {
  simpleEditor.setCursor(err_line,0);
  simpleEditor.scrollIntoView(null);
}
