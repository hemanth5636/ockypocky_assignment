var app = new Vue({

    delimiters: ['[[', ']]'],
    el: '#wrapper',
    data : {
        pageHeader : "Product Details",
        actionButtonText : "Add Product",
        showProducts : true,
        info:"something",
        addProductsEnable : false,
        subCategoriesData : null,
        errorMessage : "not saved perfectly",
        errorFlag : false,
        successFlag : false,
        productName : null,
        productDetails : null,
        selectSubCategory : 1,

    },
    methods: {
          loadSubCategoryData : function() {
            this.addProductsEnable = false
          axios
            .get('http://127.0.0.1:8000/api/v1/subcategory/')
            .then(response => {
                this.subCategoriesData = response.data.objects;
                this.addProductsEnable = true;
                console.log(this.subCategoriesData);
            })
          },
          saveProduct : function() {
            if(this.productDetails != null && this.productName != null && this.productName.length > 0
                && this.productDetails.length > 0) {
                var subCategoryUri = null;
                var categoryUri = null;
                for (var sub in this.subCategoriesData) {
                    var subObject = this.subCategoriesData[sub];
                    if(subObject.id == this.selectSubCategory) {
                        subCategoryUri = subObject.resource_uri;
                        categoryUri = subObject.category.resource_uri;
                    }
                var data = {};
                data["name"] = this.productName;
                data["details"] = this.productDetails;
                data["sub_category"] = subCategoryUri;
                }
                var saveUrl = "http://127.0.0.1:8000/api/v1/products/";
                axios
                    .post(saveUrl, data)
                    .then(Response => {
                        this.errorFlag = false;
                        this.successFlag = true;
                    })


            }
            else {
                this.errorFlag = true;
                this.errorMessage = "Data should not be empty";
            }
          },
          toggleShowProductsAndAddProduct : function() {
            if(this.showProducts) {
                this.showProducts = false;
                this.pageHeader = "Add New Product";
                this.actionButtonText = "Show Products";
                this.loadSubCategoryData();
            }
            else {
                this.showProducts = true;
                this.pageHeader = "Products Details";
                this.actionButtonText = "Add Product";
            }
          },
          toggleErrorMessage : function() {
            if(this.errorFlag)
                this.errorFlag = false;
            else
                this.errorFlag = true;
          },
          toggleSuccessMessage : function() {
            if(this.successFlag)
                this.successFlag = false;
            else
                this.successFlag = true;
          }
    }


})