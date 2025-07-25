Database design in ASP.NET Core - Mark J. Price

Hello! Here are some notes about database design from Mark J. Price, and learning tasks that are helpful.

NOTE: Yep, following his example we will certainly need to do this in a separate project since we connect to GitHub and so forth.
NOTE: We certainly do NOT need to learn every section of this chapter. But there are some key parts

Understanding Modern Databases
Relational Database Management Systems and NoSQL databases are the most common places to store data
Relational databases - SQL Server, PostgreSQL, MySQL, and SQLite
NoSQL databases: Azure Cosmos DB, Redis, Mongo DB, and Apache Cassandra

Database first: Create the database, build a model to match its structure and features. Most common scenario in real life
Code first: No database exists, so you build a model and then use EF Core to match its structure and features

Practise on sample relational database Northwind, created in 1990s

We will use SQLite as Mark J. Price suggests we do. Most common RDBMS in the world.

Learning task: Setting up SQLite for Windows

Setting up EF Core in a .NET Project
Learning task: Setting up EF Core in a .NET project
Learning task: Creating the Northwind sample database for SQLite
Downloading the Northwind database
Learning task: If you are using Visual Studio 2022
Learning task: Managing the Northwind sample database with SQLiteStudio
Nice way to see the database visually
Did not use ADO.NET as Mark does not either!
Learning task: Choosing an EF Core database provider
Basically the NuGet package for working with SQLite 3.7, or SQL Server, or MySQL, etc. that tell EF Core the appropriate classes you should use in C Sharp to effectively work with the database
Learning task: Connecting to a named SQLite database
To connect to an SQLite database we need two things 
Database path - relative to current directory or an absolute path
File name
Specify this information in a connection string (I don’t know what this is, guess we will find out!)
Learning task: Defining EF Core models
Here we connect to a database by defining an EF Core data context
The class used to represent the DB must inherit from DbContext
DbContext class can communicate with databases
Now we can define a model to represent the tables in the database (yay!)
Learning task: Defining the Northwind database context class
We can use a combination of the following to define a model
Conventions
Annotation attributes
Fluent API statements
These build an entity model at runtime which automatically update the database
An entity class represents the structure of a table
An instance of the class represents a row in that table

Defining EF Core modules
The three ways to define a model!
Learning task: Using EF Core conventions to define the model
The conventions are so simple that I will write them down for ease of use!
Table name = DbSet<T> property in DbContext class, e.g., Products
Names of columns match names of properties in entity model class, e.g., ProductId
String .NET type = nvarchar type in the database
The int .NET type = int type in the database
The primary key is a bit interesting
It is named id or ID OR
When the entity model class is named Product, the property can be named ProductId or ProductID
If this property is an integer type or the Guid type, then it is also assumed to be an IDENTITY column (column type that automatically assigns a value when inserting)
What is the Guid type? A GUID is a 128-bit integer (16 bytes) that can be used across all computers and networks wherever a unique identifier is required. Such an identifier has a very low probability of being duplicated.
There are many more conventions, and you can even define your own. But that is beyond the scope of this book. So don’t worry about it!
Learning task: Using EF Core annotation attributes to define the model
Conventions are usually not enough to completely map the classes to the database objects
Some common attributes are mentioned in the book. 
[Required] = Value is not null
[StringLength(50)] = Value is up to 50 characters in length
[Column(TypeName = “money”, Name = “Unit-Price”)] = Specify the column type and column name used in the table
There is another table with more common attributes. I invite you to explore these as you build projects!
Here is a very specific example of a mapping between some Data Definition Language (DDL) code and an EF Core annotation attribute
DDL code excerpt: ProductName NVARCHAR (40) NOT NULL
Product class excerpt:
[Required]
[StringLength(40)]
Public string ProductName {get; set;}
What about if there is no map between types? Like, column type NVARCHAR maps to string, but what if we have column type money?
Refer to this example
DDL code excerpt: UnitPrice "MONEY" CONSTRAINT DF_Products_UnitPrice DEFAULT (0)
Product class excerpt:
[Column(TypeName = “money”)]
Public decimal? UnitPrice {get; set}
Note how the attribute is used, and the type used in the product class
Learning task: Using the EF Core Fluent API to define the model
You can use this instead of attributes, or in addition to them
With the ProductName example, you could write the following Fluent API statement in the OnModelCreating method of the database context class as shown
modelBuilder.Entity<Product>()
  .Property(product => product.ProductName)
  .IsRequired()
  .HasMaxLength(40);
Note: The OnModelCreating method is written as a separate method in NorthwindDb.cs file
Benefit: The entity model class itself is simpler
Benefit 2: You can ensure that a database is populated with certain data! 

Learning task: Building EF Core models for the Northwind tables
Create a class library, placed within chapter 10 directory
Make sure that you can see the Northwind.EntityModels in your chapter 10 solution, otherwise you need to add it. Do this from the Solution Explorer
Learning task: Defining the Category and Product entity classes
We don't need to include all columns from a table as properties!
When making a new row those columns will be null or some other default value
So make sure those columns are optional or have a default value!
We can rename a column by defining a property with a different name, like Cost, and then decorating the property with the [Column] attribute and specifying its column name, like UnitPrice. The final property, CategoryId, is associated with a Category property that will be used to map each product to its parent category.
There are some other interesting things that I wrote as comments in the classes. Feel free to refer to them if you get confused!
Learning task: Adding tables to the Northwind database context class
Within the general project you must update the C# file with properties for the database to give the context for the tables represented within the entity models
If you WANT to use Fluent API to decorate your entity classes, do it within the aforementioned file
Learning task: Setting up the dotnet-ef tool
We have set up the entity models manually, but screw that. We can have the work done for us!
You must have dotnet-ef first though, so check that
Learning task: Scaffolding models using an existing database
Also, PLEASE keep on running your csproj throughout to catch bugs. Just spent 10 minutes figuring out why my project was failing to build!
Even if you scaffold, do not be scared to correct the approximation that the machine makes! Especially if you do not expect to scaffold again!
There are differences but I can’t be asked to enumerate them. Don’t worry about them bro
Learning task: Configuring preconvention models
You can manually add conventions, like making sure that all strings mentioned in models only take 50 characters without explicitly putting this for every string mention
We will use the classes that we manually created


Querying EF Core Modules
Now we will write some LINQ queries and see the output (more on this in the LINQ chapter)
We use two partial classes to generate a query on the database and display it to the console, both within Program
Program.helpers.cs allows us to print to console
Program.Queries.cs allows us to query the database
Learning task: Filtering included Entities
We use “filtered includes”, a method to filter the entities that are returned
Note that this method is written within the Program.Queries.cs file and that it is distinct from the previous method written
Learning task: Filtering and sorting products
We define a QueryingProducts method
All we are doing here is filtering like in the previous task, but now we sort the results so that there is an order to how they are displayed on the console
Note the decreasing order by cost
Learning task: Getting the generated SQL
How well written are the SQL statements generated by these C# queries?
Literally one line to write per foreach statement in the partial classes to output the generated SQL
We do this in the FilteredIncludes method and the QueryingProducts method
Learning task: Logging EF Core
We can even monitor the interaction between EF Core and the database
We write this in NorthwindDb.cs
Learning task: Filtering logs by provider-specific values
Here we tell the Program to only show the log information where EF Core and the database translate the LINQ queries into SQL
Learning task: Logging with query tags
We can add SQL comments to the log to correlate log messages
Useful for complex scenarios
Note that in this example we add a single line to Program.Queries.cs
Run from NorthwindDb.cs and run the queries as in the previous learning tasks. You will see the comment just before the program ends
Learning task: Getting a single entity
There are two LINQ methods to get a single entity: First and Single
First uses LIMIT 1, Single uses LIMIT 2. Why?
For First, the query can match one or more entities and only the first will be returned. If there is only one then an exception will be thrown.
Therefore First only checks against a single instance
For Single, the query must match only one entity and it will be returned. If there is more than one match, an exception must be thrown
Therefore Single checks that there is one instance and no second instance!
Good practice: If you do not need to make sure that only one entity matches, use First instead of Single to avoid retrieving two records!
Learning task: Pattern matching with Like
We can even use Like
In this example you can write a partial product name and query for all matching product names
Learning task: Generating a random number in queries
We have a useful function that maps to the database function for generating a random number
For example, you could perform ROWS*random_number() (pseudo-code) to select a random row
Learning task: Defining global filters
In the Northwind database, products can be discontinued
We use a global filter to avoid showing discontinued products

Loading and tracking patterns with EF Core
Eager loading: Load data early
Lazy loading: Load data automatically just before it is needed <- Sounds great to me!
Explicit loading: Load data manually

Learning task: Eager loading entities using the Include extension method
I don’t really get it, but for some reason you get 0 for everything
Oh wait, by removing the Include extension method we prevent the use of Eager Loading, so we have no data to display!
Learning task: Enabling lazy loading
Now we introduce a package of EF Core proxies
We get the data JIT, which means possibly more queries sent
We had disabled eager loading, and have now introduced lazy loading. Therefore, we have data to display!
Learning task: Explicit loading entities using the Load method
We introduce code so that we can choose between Explicitly loading the data or eagerly loading the data
Explicit Load sees us choose each instance of data we want to load
Eager Load sees us load all the data as before
Good Practise: Consider which loading pattern is best for your code!
Learning task: Controlling the tracking of entities
This is kind of complex, so try to follow along step by step
Entity Identity Resolution: EF core resolves each entity instance by reading its unique primary key value
Therefore keyless entities are never tracked
EF Core assumes that you want to track entities in local memory, so you can call SaveChanges to make any changes in local memory to the underlying data store
This improves efficiency
Scenario: 
There is a database about customers by country
You query for all German customers into the context
After five minutes you query for all customers whose names start with A
EF Core will not update the data in the context for the second query regarding German customers
What if the telephone information for a German customer whose name begins with A changes in the underlying data store?
EF Core never checked the data for that customer, so their telephone information does not change!
If you do not need to track local changes, or you want to load new instances of an entity for every query execution, you can disable tracking!
Uses the AsNoTracking method
Multiple options are given, and it seems that you would manually write the code in NorthwindDb.cs or Program.Queries.cs
Since we are not so interested we have not written the code for this
Learning task: Three tracking scenarios
No code here! This is just pure theory to help understand some tracking scenarios
Note: tables are available for reference
Default tracking
This is tracking with identity resolution
An entity loaded into the data context has no underlying changes reflected, only one copy exists locally
A call to SaveChanges updates the database
No tracking and no identity resolution
Every query loads another instance of a database row into the data context
This includes underlying changes, allowing duplicates and mixed out-of-data and updated data
No local entity changes are tracked, so SaveChanges does nothing!
No tracking with identity resolution
Once an entity is loaded into the data context, underlying changes are not reflected and only one copy exists
No local entity changes are tracked, so SaveChanges does nothing!
Learning task: Lazy loading for no tracking queries
EF Core enables support for lazy loading of entities that are not being tracked
Learning task: Summary of tracking
You can choose the tracking that you want!
Keep in mind the trade-offs of course, and stick to this theory. 
Blog posts may claim that AsNoTracking improves EF Core queries, but you know that running the same query that returns thousands of queries will make your data context unnecessarily busy!


Modifying data with EF Core

HOLY HELL, ChatGPT helped me here. Dotnet clean then dotnet rebuild to prevent using old code! 

Crud is easy using EF Core
DbContext maintains change tracking (CRUD) automatically
Call SaveChanges when you want to save local change tracking to the database

Learning task: Inserting entities
We add a new row to a table!
We also read
Not much more to say
Learning task: Updating entities
Note that in a real application you should refer to the UID, not the name
Learning task: Deleting entities

Okay, for now just note that this chapter kept on failing until I did the following
In terminal
dotnet clean
dotnet build
dotnet run --project WorkingWithEFCore.csproj
Just like that. If you do that then you are good. 

HOLY FUCK, WAIT, IF CLEAN DOESN’T WORK…
Check which Visual Studio you are on.
I must have been in VS 2019 which is too old. Check you are on VS 2022!


Learning task: More efficient updates and deletes
That was the traditional way of CRUD. You can see the steps in the book

Now we can use ExecuteDelete and ExecuteUpdate to make update and delete operations more efficient!

You can only ExecuteUpdate and ExecuteDelete on a single table


Learning task: Pooling database contexts
I don’t really care. Something about pooling DbContexts that .NET Core does automatically which makes websites made efficient


Learning task: Learning and exploring
Test your knowledge and understanding by answering some questions, getting some hands-on practise, and exploring this chapter’s topics with deeper research.

Er, no I will not.
I am still following the John Sonmez school of thought. I will learn as I develop that Scrum product. I will use the completed project and these notes when I hit an issue. Ura!
Also some exercises are good, but looking at “exercise 10.3 - working with transactions” and “exercise 10.6 - Explore topics” I will pass on those exercises. We have not covered transactions. 

We are doing a top-down dynamic programming approach, not bottom-up. If we hit an issue we come to here and the project. If we are still stuck and GPT doesn’t help, then okay.

Here are the exercises if you care about them
Exercise 10.1 - Test your knowledge <- the most useful exercise
Exercise 10.2 - Exporting data using different serialisation formats
Exercise 10.3 - Working with transactions
Exercise 10.4 - Explore a Code First EF Core model
Exercise 10.5 - Explore app secrets
Exercise 10.6 - Explore topics
Exercise 10.7 - Explore NoSQL databases

Learning task: Summary
In this chapter, you learned how to
Connect to and build entity data models for an existing database
Execute a simple LINQ query and process the results 
Use filtered includes
Control loading and tracking patterns
Add, modify, and delete data
