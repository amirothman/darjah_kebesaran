var page = require('webpage').create();

page.open('http://www.istiadat.gov.my/index.php/component/semakanlantikanskp/', function() {
  page.includeJs("http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js", function() {
    page.evaluateJavaScript('window.submitpaging(3)');
    console.log(page.content);
    phantom.exit()
  });



});
