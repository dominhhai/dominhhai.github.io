// KaTex Math Config
var katexOpts = { delimiters:[
  { left: "$$"  , right: "$$"  , display: true  },
  { left: "\\[" , right: "\\]" , display: true  },
  { left: "$"   , right: "$"   , display: false },
  { left: "\\(" , right: "\\)" , display: false }
]};
// render KaTex Math
renderMathInElement(document.body, katexOpts);

// Language Select
$('#language').on('change', function() {
  window.location.pathname = window.location.pathname.replace(/\/(.*?)\//i, '/'+ this.value +'/');
});

// Editor
$('#editor textarea').on('input change', function() {
  var preview = document.getElementById('preview-content');
  var rawTxt = this.value.trim();
  if (rawTxt.length < 1) {
    return preview.innerHTML = rawTxt;
  }
  // to markdown
  preview.innerHTML = marked(rawTxt);
  // to KaTeX Math
  renderMathInElement(preview, katexOpts);
});
