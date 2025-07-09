using Microsoft.AspNetCore.Mvc;

namespace AreteTechnologiesSite.Controllers
{
    public class ScrumController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
