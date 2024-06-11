---
seoDescription: Do you know how to use code migrations? Manage database schemas effectively with Entity Framework Code First Migrations. Update a production database schema without recreating it from scratch.
type: rule
title: Do you know to use code migrations?
uri: use-code-migrations
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
related:
  - tools-database-schema-changes
created: 2021-12-13T17:27:38.786Z
guid: 8284cedd-8eea-4e3b-b04b-451896a615c0
---

Most enterprise applications require a database to store data. Once you have a database you need a way to manage the schema.

Entity Framework Code First Migrations allow you to update a database schema rather than recreate it from scratch. This is useful when you have a production database that you want to keep, but you want to make changes to the schema.

<!--endintro-->

## Database Schema Management Options

Managing database schemas effectively is crucial for the smooth operation and evolution of software applications. For more options to manage database schemas, see [the best tools for updating database schemas](/tools-database-schema-changes/).

## Configuring Entity Framework Code First Migrations

The following assumes you have an existing project with a database context, entities, and have already installed the EF Core nuget packages.

1. Install EF Core Tools

   ```bash
   dotnet new tool-manifest
   dotnet tool install dotnet-ef
   ```

2. Enable migrations

   ```bash
   dotnet ef migrations add InitialCreate
   ```

   This will create a migration file in your project. This file contains the code to create the database schema.

   ```cs
   // Example of EF Core Migration in a .NET 8 project
   public partial class AddUserTable : Migration
   {
       protected override void Up(MigrationBuilder migrationBuilder)
       {
           migrationBuilder.CreateTable(
               name: "Users",
               columns: table => new
               {
                   Id = table.Column<int>(nullable: false)
                       .Annotation("SqlServer:Identity", "1, 1"),
                   Name = table.Column<string>(nullable: true)
               },
               constraints: table =>
               {
                   table.PrimaryKey("PK_Users", x => x.Id);
               });
       }

       protected override void Down(MigrationBuilder migrationBuilder)
       {
           migrationBuilder.DropTable(
               name: "Users");
       }
   }

   ```

3. Update database

   ```bash
   dotnet ef database update
   ```

### Using Rider

If you struggle to remember the commands above, Rider has a great UI that makes creating migrations easy. This is especially useful when you have different projects for both startup and migrations.

::: img-large  
![Rider - EF Core Migrations](rider-ef-core.png)
:::

## Executing Entity Framework Code First Migrations

Once you have some migration, you'll then need to decide when these get run. Naively, developers will often run migrations during program start-up, but this is not recommended. Doing so can cause issues in a web farm environment, as well as cause unnecessary delays during start-up.

```csharp
var dbContext = scope.ServiceProvider.GetRequiredService<EagleEyeDbContext>();
await dbContext.Database.MigrateAsync();
```

::: bad
Figure: Bad example - Running migrations manually during startup in `program.cs`
:::

### Entity Framework Migration Bundles

A place to run migrations is during your CICD deployment pipeline.

```bash
dotnet ef migrations bundle --self-contained --force
.\efbundle.exe --connection {$ENVVARWITHCONNECTION}
```

::: good
Figure: Good example - Creating and executing a migration bundle during a CICD pipeline
:::

::: info  
If an `appsettings.json` file can be found the connection string can be automatically picked up.
:::
