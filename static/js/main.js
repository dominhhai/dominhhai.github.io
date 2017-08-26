$('#language').on('change', function() {
  window.location.pathname = window.location.pathname.replace(/\/(.*?)\//i, '/'+ $(this).val() +'/')
})
