const arr = [];
const cart = [];
const showCart = [];
const input = document.getElementById("value");
const optionsVal = document.getElementById("list");
const dropdown = document.getElementById("dropdown");
const productValue = document.getElementById("productValue");
const customerPhone = document.getElementById("customerPhone");
const customerName = document.getElementById("customerName");
const loading = document.getElementById("loading");
const message = document.getElementById("message");

dropdown.style.display = "none";
loading.style.display = "none";

const clearMessage = () => {
	setTimeout(() => {
		message.innerHTML = "";
	}, 5000);
};

const showMessage = (type = "info", text) => {
	message.innerHTML = "";
	const output = `
		<div class="alert alert-${type} alert-dismissible fade show" role="alert">
			${text}
			<button type="button" class="close" data-dismiss="alert" aria-label="Close">
				<span aria-hidden="true">&times;</span>
			</button>
		</div>
	`;
	message.innerHTML = output;
	clearMessage();
};

// fetch products
const fetchProducts = async () => {
	let response = await fetch("/api/v1/product");
	let data = await response.json();
	arr.push(...data);
};
fetchProducts();

// get customer
const getCustomer = async (phone) => {
	const url = `/api/v1/customer?phone=${phone}`;
	loading.style.display = "block";
	let response = await fetch(url);
	let data = await response.json();
	if (data.customer) {
		customerName.value = data?.customer?.name;
		console.log(data);
	} else {
		customerName.value = "";
		showMessage("danger", "Customer not found.");
	}
	console.log("loading off");
	loading.style.display = "none";
};

console.log(arr);

// string to slug
const string_to_slug = (str) => {
	str = str.replace(/^\s+|\s+$/g, ""); // trim
	str = str.toLowerCase();

	// remove accents, swap ñ for n, etc
	let from = "àáãäâèéëêìíïîòóöôùúüûñç·/_,:;";
	let to = "aaaaaeeeeiiiioooouuuunc------";

	for (let i = 0, l = from.length; i < l; i++) {
		str = str.replace(new RegExp(from.charAt(i), "g"), to.charAt(i));
	}

	str = str
		.replace(/[^a-z0-9 -]/g, "") // remove invalid chars
		.replace(/\s+/g, "-") // collapse whitespace and replace by -
		.replace(/-+/g, "-"); // collapse dashes

	return str;
};

//shows the list
const show = () => {
	dropdown.style.display = "none";

	optionsVal.options.length = 0;

	if (input.value) {
		dropdown.style.display = "block";
		const textProduct = string_to_slug(input.value);

		for (let i = 0; i < arr.length; i++) {
			if (arr[i].product_slug.indexOf(textProduct) !== -1) {
				//addvalue
				addValue(arr[i].product_name, arr[i].id);
				optionsVal.size = optionsVal.options.length;
			}
		}
	}
};

const addValue = (text, val) => {
	const createOptions = document.createElement("option");
	optionsVal.appendChild(createOptions);
	createOptions.text = text;
	createOptions.value = text;
	productValue.value = val;
};

//Settin the value in the box by firing the click event
const setVal = (selectedVal) => {
	input.value = selectedVal.value;
	document.getElementById("dropdown").style.display = "none";
};

const showCartItems = () => {
	let output = "";
	showCart.forEach((item) => {
		output += `
			<tr>
				<td>${item.name}</td>
				<td>${item.price}</td>
				<td>${item.quantity}</td>
				<td>
					<button class="btn btn-outline-danger btn-sm">
						<i class="fa fa-trash-alt"></i>
					</button>
				</td>
			</tr>
		`;
	});
	document.getElementById("cartData").innerHTML = output;
};

// add product to cart
const addProductToCart = () => {
	const productValue = document.getElementById("productValue");
	const productPrice = document.getElementById("productPrice");
	const productQuantity = document.getElementById("productQuantity");

	if (
		productValue.value !== "" &&
		productPrice.value > 0 &&
		productQuantity.value > 0
	) {
		let product = {
			id: productValue.value,
			price: productPrice.value,
			quantity: productQuantity.value,
		};
		let showProduct = {
			name: input.value,
			price: productPrice.value,
			quantity: productQuantity.value,
		};
		cart.push(product);
		showCart.push(showProduct);
		showCartItems();
		productValue.value = "";
		productPrice.value = "";
		productQuantity.value = "";
		input.value = "";
	} else {
		console.log("error");
	}
};

// remove product to local storage
function removeProduct(productId) {
	// Your logic for your app.

	// strore products in local storage

	let storageProducts = JSON.parse(localStorage.getItem("products"));
	let products = storageProducts.filter(
		(product) => product.productId !== productId
	);
	localStorage.setItem("products", JSON.stringify(products));
}

// Event listeners
input.addEventListener("keyup", show);

optionsVal.onclick = function () {
	setVal(this);
};

customerPhone.onblur = () => {
	phone = customerPhone.value;
	getCustomer(phone);
};
