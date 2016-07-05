
var casper = require('casper').create();
casper.start('http://www.istiadat.gov.my/index.php/component/semakanlantikanskp/');

casper.then(function() {
    this.submitpaging('1')
    console.log("aasas")
});

casper.thenOpen('http://phantomjs.org', function() {
    this.echo('Second Page: ' + this.getTitle());
});

casper.run();
