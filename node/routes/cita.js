const exprres = require("express");
const router = exprres.Router();
const citaController = require("../controllers/cita");

router.get("/todas", citaController.todas);
router.post("/registrar", citaController.registrar);
router.get("/buscar/:id", citaController.buscar);
router.post("/modificar/:id", citaController.modificar);
router.delete("/eliminar/:id", citaController.elimnar);

module.exports = router;
