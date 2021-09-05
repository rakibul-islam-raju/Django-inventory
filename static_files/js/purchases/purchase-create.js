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
			errorMessages: null,
			successMessages: null,

			errors: [],
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
					document.getElementById("warehouseModalClose").click();
					this.warehouseName = null;
					this.warehouseDescription = null;
					this.successMessages =
						"Warehouse was created successfully.";
				})
				.catch(function (error) {
					this.errorMessages = "Network Error";
				});
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
					document.getElementById("categoryModalClose").click();
					this.categoryName = null;
					this.categoryDescription = null;
					this.successMessages = "Category was created successfully.";
				})
				.catch(function (error) {
					this.errorMessages = "Network Error";
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
					document.getElementById("subcategoryModalClose").click();
					this.subcategoryCategory = null;
					this.subcategoryName = null;
					this.subcategoryDescription = null;
					this.successMessages =
						"Subcategory was created successfully.";
					status = true;
				})
				.catch((error) => {
					console.log(error);
				})
				.finally(() => {
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
