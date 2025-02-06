## the problem in first test case Address verify is due to missing feild zip in json data
that is fixed with addition of zip : 06810

## the second assemement 
is to add a get request to fetch data of shipment with id shp_e0b570fd1d7d4b62bd206917eae5881a

## the third was about adding test case
i have duplicate second get request and add js script to validate 
• Verify that value of selected_rate. retail_rate is equals to 12
• Verify that retail_rate is greater than list_rate

using 
```
pm.test("Response body has no errors", function () {
    pm.expect(pm.response.text()).to.include("\"errors\":[]");
});

pm.test("Response ZIP verified", function () {
    pm.expect(pm.response.text()).to.include("06810");
});

```