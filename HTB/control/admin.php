<?php
$allowed = array('192.168.4.28');
if (!isset($_SERVER['HTTP_X_FORWARDED_FOR'])) {
	$_SERVER['HTTP_ORIGIN'] = $_SERVER['REMOTE_ADDR'];
}
if (in_array($_SERVER['HTTP_X_FORWARDED_FOR'], $allowed)) { } else {
	die('Access Denied: Header Missing. Please ensure you go through the proxy to access this page');
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
	<title>Fidelity</title>
	<meta charset="utf-8">
	<script type="text/javascript" src="assets/js/functions.js"></script>
	<script type="text/javascript" src="assets/js/checkValues.js"></script>
	<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
	<link rel="stylesheet" href="assets/css/main.css" />
	<noscript>
		<link rel="stylesheet" href="assets/css/noscript.css" />
	</noscript>
</head>

<body class="is-preload landing">
	<div id="main" class="wrapper style1">
		<div class="container">

			<!-- Header -->
			<header id="header">
				<h1 id="logo"><a href="index.php">Fidelity</a></h1>
				<nav id="nav">
					<ul>
						<li><a href="index.php">Home</a></li>
						<li><a href="about.php">About</a></li>
						<li><a href="admin.php">Admin</a></li>
						<li><a href="index.php" class="button primary">Logout</a></li>
					</ul>
				</nav>
			</header>

			<!-- Search -->
			<section>
				<div>
					<h2>Find Products</h2>
					<form id="searchProducts" action="search_products.php" method="POST">
						<div class="row gtr-uniform gtr-50">
							<div class="col-8 col-12-xsmall"><input type="text" name="productName" id="productName" placeholder="Name" /></div>
							<div class="col-4 col-12-xsmall"><input type="submit" value="Search" class="primary" /></div>

						</div>
					</form>
				</div>
			</section>

			<!-- Latest Products -->
			<section>
				<h2>Latest Products</h2>
				<div class="table-wrapper">
					<table border="1" cellpadding="10">
						<thead>
							<tr>
								<th>Name</th>
								<th>Quantity</th>
								<th>Action</th>
							</tr>
						</thead>
						<tbody>
							<form id="viewProducts" method="POST">
								<input type="hidden" id="productId" name="productId" value="" />
								<?php
								include 'database.php';
								$pdo = Database::connect();
								$sql = 'SELECT * FROM product ORDER BY name ASC limit 5';
								foreach ($pdo->query($sql) as $product) {
									echo "<tr>";
									echo '<td>' . $product['name'] . '</td>';
									echo '<td>' . $product['quantity'] . '</td>';
									echo '<td><div class="row">';
									echo '<button class="button  small" type="button" onclick="viewProduct(' . $product['id'] . ')">View</button>';
									echo '&nbsp;<button class="button small" type="button" onclick="updateProduct(' . $product['id'] . ')">Update</button>';
									echo '&nbsp;<button class="button  small" type="button" onclick="deleteProduct(' . $product['id'] . ')">Delete</button></td>';
									echo '</td></div></tr>';
								}
								?>
							</form>
						</tbody>
					</table>
				</div>
			</section>
			<!-- Create Product -->
			<section>
				<h2>Create Product</h2>
				<form id="createProduct" action="create_product.php" method="POST" onsubmit="return checkValues('createProduct')">
					<table border="1" cellpadding="10">
						<thead>
							<tr>
								<th>Name</th>
								<th>Quantity</th>
								<th>Category</th>
								<th>Price</th>
							</tr>
						</thead>
						<tbody>
							<td><input name="name" type="text" value="" /></td>
							<td><input name="quantity" type="text" value="" /></td>
							<td><select name="category">
									<?php
									$sql = "SELECT * FROM product_category ORDER BY category ASC;";
									foreach ($pdo->query($sql) as $category) {
										echo '<option value="' . $category['id'] . '">' . $category['category'] . '</option>';
									}
									?>
								</select>
							</td>
							<td>
								<input name="price" type="text" value="" />
							</td>
						</tbody>
					</table>
					<ul class="actions">
						<li><button type="submit" class="button primary small">Create</button></li>
					</ul>
				</form>
			</section>
			<br>
			<br>
			<!-- Categories -->
			<section>
				<h2>Categories</h2>
				<div class="table-wrapper">
					<table border="1" cellpadding="10">
						<thead>
							<tr>
								<th>Name</th>
								<th>Action</th>
							</tr>
						</thead>
						<tbody>
							<form id="categoryOptions" method="POST" onsubmit="return checkValues('updateCategory')">
								<input type="hidden" id="categoryId" name="categoryId" value="" />
								<?php
								$sql = 'SELECT * FROM product_category ORDER BY id ASC';
								foreach ($pdo->query($sql) as $category) {
									echo "<tr>";
									if ($category['id'] != 1) {
										echo '<td><input name="name" type="text" value="' . $category['category'] . '" /></td>';
										echo '<div class="col-3 col-6-medium col-12-xsmall">';
										echo '<td><button class="button small" type="button" onclick="updateCategory(' . $category['id'] . ')">Update</button>';
										echo '&nbsp;<button class="button small" type="button" onclick="deleteCategory(' . $category['id'] . ')">Delete</button></td>';
									} else {
										echo '<td>' . $category['category'] . '</td>';
										echo "<td>Not Allowed</td>";
									}
									echo '</tr>';
								}
								Database::disconnect();
								?>
							</form>
						</tbody>
					</table>
				</div>
			</section>
			<!-- Create Category -->
			<section>
				<h2>Create Category</h2>
				<form id="createCategory" action="create_category.php" method="POST" onsubmit="return checkValues('createCategory')">
					<div class="row gtr-uniform gtr-50">
						<div class="col-4 col-12-xsmall"><input type="text" name="categoryName" id="categoryName" placeholder="Name" /></div>
						<div class="col-4 col-12-xsmall"><input type="submit" value="Create" class="primary" /></div>
					</div>
				</form>
			</section>
		</div>
		<!-- Footer -->
		<footer id="footer">
			<ul class="icons">
				<li><a href="#" class="icon brands alt fa-twitter"><span class="label">Twitter</span></a></li>
				<li><a href="#" class="icon brands alt fa-facebook-f"><span class="label">Facebook</span></a></li>
				<li><a href="#" class="icon brands alt fa-linkedin-in"><span class="label">LinkedIn</span></a></li>
				<li><a href="#" class="icon brands alt fa-instagram"><span class="label">Instagram</span></a></li>
				<li><a href="#" class="icon brands alt fa-github"><span class="label">GitHub</span></a></li>
				<li><a href="#" class="icon solid alt fa-envelope"><span class="label">Email</span></a></li>
			</ul>
			<ul class="copyright">
				<li>&copy; Fidelity. All rights reserved.</li>
			</ul>
		</footer>
	</div>
	<!-- Scripts -->
	<script src="assets/js/jquery.min.js"></script>
	<script src="assets/js/jquery.scrolly.min.js"></script>
	<script src="assets/js/jquery.dropotron.min.js"></script>
	<script src="assets/js/jquery.scrollex.min.js"></script>
	<script src="assets/js/browser.min.js"></script>
	<script src="assets/js/breakpoints.min.js"></script>
	<script src="assets/js/util.js"></script>
	<script src="assets/js/main.js"></script>
</body>

</html>