const exprres = require("express");
const router = exprres.Router();
const citaController = require("../controllers/cita");

router.get("/todas", citaController.todas);
router.post("/registrar", citaController.registrar);
router.get("/buscar", citaController.buscar);
router.post("/modificar/:id", citaController.modificar);
router.delete("/eliminar/:id", citaController.elimnar);
router.get("/buscar_id/:id", citaController.buscar_id);

module.exports = router;
