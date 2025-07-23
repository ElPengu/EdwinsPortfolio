using Northwind.EntityModels; // To use Northwind.

// Commented out when calling methods within
// partial classes
/*
//Create a Northwind instance
//using NorthwindDb db = new();
//Output the database provider name
//WriteLine($"Provider: {db.Database.ProviderName}");
// Disposes the database context.
*/

//Commented out when calling methods from
//QueryingWithLike and onwards

// Within Program.Helpers.cs partial class
ConfigureConsole();

// Within Program.Queries.cs partial class
//QueryingCategories();

// Query against a minimum of 100 for example
//FilteredIncludes();

// Query against a cost of 50 for example
// Note the descending order by cost
// On another run try 500
//QueryingProducts();

// Enter 1 for product ID
// Note the difference between First and Single
// With First, Limit is 1 because it looks for 
// the first instance of that ID
// With Single, Limit is 2 because it looks for 
// the first instance of that ID AND checks that 
// there is no other instance
//GettingOneProduct();


// Try entering a partial product name like che
// Now that now we do not show discontinued products, 
// Note the missing Chef Anton's Fumbo Mix when
// you enter a partial product name like che
//QueryingWithLike();

// How do we get a random product? By using a
// random number function within the method!
// Note it runs automatically, no input!
//GetRandomProduct();

LazyLoadingWithNoTracking();