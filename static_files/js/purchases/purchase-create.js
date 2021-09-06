const purchaseForm = {
	data() {
		return {
			// payment option toggle
			paymentMethod: "",
			bankOption: false,
			// add warehouse
			warehouseName: "",
			warehouseDescription: "",
			// add category
			categoryName: "",
			categoryDescription: "",
			// add subcategory
			subcategoryCategory: "",
			subcategoryName: "",
			subcategoryDescription: "",
			// sub category list
			subcategories: [],
			selectSubcategories: [],
			// dependent subcategory dropdown
			categoryOption: null,
			subcategoryOption: null,
			// error messages
			formErrors: [],
			errorMessage: "",
			successMessage: "",
		};
	},
	methods: {
		fetchSubcategory() {
			axios.get("/api/v1/subcategory").then((response) => {
				this.subcategories = response.data;
			});
		},

		paymentBank() {
			if (this.paymentMethod == "bank") {
				this.bankOption = true;
			} else this.bankOption = false;
		},

		createWarehouse() {
			axios.defaults.xsrfCookieName = "csrftoken";
			axios.defaults.xsrfHeaderName = "X-CSRFToken";
			axios
				.post("/api/v1/warehouse", {
					name: this.warehouseName,
					description: this.warehouseDescription,
				})
				.then(function (response) {
					const select = document.getElementById("id_warehouse");
					const opt = new Option(
						`${response.data.name}`,
						`${response.data.id}`
					);
					select.insertBefore(opt, select.firstChild);
					this.warehouseName = null;
					this.warehouseDescription = null;
					this.successMessages =
						"Warehouse was created successfully.";
				})
				.catch(function (error) {
					if (error.response) {
						this.formErrors = error.response.data;
					} else {
						this.errorMessage = "Network Error";
					}
				})
				.finally(() =>
					document.getElementById("warehouseModalClose").click()
				);
		},

		createCategory() {
			axios.defaults.xsrfCookieName = "csrftoken";
			axios.defaults.xsrfHeaderName = "X-CSRFToken";
			axios
				.post("/api/v1/category", {
					name: this.categoryName,
					description: this.categoryDescription,
				})
				.then(function (response) {
					const select = document.getElementById("id_category");
					const opt = new Option(
						`${response.data.name}`,
						`${response.data.id}`
					);
					select.insertBefore(opt, select.firstChild);

					this.categoryName = null;
					this.categoryDescription = null;
					this.successMessages = "Category was created successfully.";
				})
				.catch(function (error) {
					if (error.response) {
						console.log(error.response.data);
						this.formErrors = error.response.data;
						console.log(this.formErrors);
					} else {
						this.errorMessage = "Network Error";
					}
				})
				.finally(() => {
					document.getElementById("categoryModalClose").click();
					console.log(this.formErrors);
				});
		},

		createSubCategory() {
			let status = null;
			axios.defaults.xsrfCookieName = "csrftoken";
			axios.defaults.xsrfHeaderName = "X-CSRFToken";
			axios
				.post("/api/v1/subcategory", {
					category: this.subcategoryCategory,
					name: this.subcategoryName,
					description: this.subcategoryDescription,
				})
				.then((response) => {
					this.subcategoryCategory = null;
					this.subcategoryName = null;
					this.subcategoryDescription = null;
					this.successMessages =
						"Subcategory was created successfully.";
					status = true;
				})
				.catch((error) => {
					if (error.response) {
						this.formErrors = error.response.data;
					} else {
						this.errorMessage = "Network Error";
					}
				})
				.finally(() => {
					document.getElementById("subcategoryModalClose").click();
					if (status === true) {
						this.fetchSubcategory();
						this.selectSubcategory();
					}
				});
		},

		selectSubcategory() {
			const select = document.getElementById("id_category");
			const value = select.options[select.selectedIndex].value;
			const returnedSubcats = this.subcategories.filter(
				(subcat) => subcat.category == parseInt(value)
			);
			this.selectSubcategories = returnedSubcats;
		},
	},
	mounted() {
		this.fetchSubcategory();
	},
	delimiters: ["[[", "]]"],
};

Vue.createApp(purchaseForm).mount("#purchase-create");
