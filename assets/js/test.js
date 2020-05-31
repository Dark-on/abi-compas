describe("showSlide", function() {

    before(function() { alert("Start of tests"); });
    after(function() { alert("End of tests"); });
  
    beforeEach(function() { alert("Entry in test"); });
    afterEach(function() { alert("Exit from test"); });

    it("When the input index is 4, the result is: 0", function() {
      assert.equal(showSlide(4), 0);
    });
    
    it("When the input index is 1, the result is: 1", function() {
        assert.equal(showSlide(1), 1);
      });
      
    it("When the input index is 2, the result is: 2", function() {
        assert.equal(showSlide(2), 2);
      });
      
    it("When the input index is -1, the result is: 3", function() {
        assert.equal(showSlide(-1), 3);
      });
      
    it("When the input index is 0, the result is: 0", function() {
        assert.equal(showSlide(0), 0);
      });
  
  });
  
  describe("customizeTimer", function() {

    before(function() { alert("Start of tests"); });
    after(function() { alert("End of tests"); });
  
    beforeEach(function() { alert("Entry in test"); });
    afterEach(function() { alert("Exit from test"); });

    it("When the input May 20, 2020 00:00:00 output:", function() {
      assert.equal(customizeTimer(new Date("May 20, 2020 20:00:30")), "Пора здавати проект");
    });
    
    it("When the input is June 21, 2020 00:04:00, the result is: 1", function() {
        assert.equal(customizeTimer(new Date("June 21, 2020 00:04:00")), "19 days 22:52:19");
      });
      
    it("When the input is May 25, 2020 00:20:01, the result is: 2", function() {
        assert.equal(customizeTimer(new Date("May 25, 2020 00:20:01")), "Пора здавати проект");
      });
      
    it("When the input is July 10, 2020 10:30:00, the result is: 3", function() {
        assert.equal(customizeTimer(new Date("July 10, 2020 10:30:00")), "39 days 09:18:19");
      });
      
    it("When the input is May 28, 2020 01:00:00, the result is: 0", function() {
        assert.equal(customizeTimer(new Date("September 28, 2020 01:00:00"))2, "118 days 23:48:19");
      });
  
  });