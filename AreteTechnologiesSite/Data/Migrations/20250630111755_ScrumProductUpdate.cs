using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace AreteTechnologiesSite.Data.Migrations
{
    /// <inheritdoc />
    public partial class ScrumProductUpdate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "ProductEpic",
                table: "Scrum_Product");

            migrationBuilder.DropColumn(
                name: "ProductStory",
                table: "Scrum_Product");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "ProductEpic",
                table: "Scrum_Product",
                type: "nvarchar(max)",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "ProductStory",
                table: "Scrum_Product",
                type: "nvarchar(max)",
                nullable: false,
                defaultValue: "");
        }
    }
}
