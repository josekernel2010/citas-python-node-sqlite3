const conexion = require("../conexion");

const todas = (req, res) => {
  const sql = `select * from cita`;
  conexion.all(sql, (err, result) => {
    if (err) {
      res.send("Ha ocurrido un error: " + err);
    } else {
      res.send(result);
    }
  });
};

const buscar = (req, res) => {
  const fecha = req.body.fecha;
  const sql = `select * from cita where fecha = '${fecha}' and estado = 'Agendada'`;
  conexion.all(sql, (err, result) => {
    if (err) {
      res.send("Ha ocurrido un error: " + err);
    } else {
      res.send(result);
    }
  });
};

const registrar = (req, res) => {
  const { paciente, detalle, fecha, hora, estado } = req.body;

  const sql = `insert into cita(paciente, detalle, fecha, hora, estado)
   values('${paciente}', '${detalle}', '${fecha}', '${hora}', '${estado}')`;

  conexion.run(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error: " + err);
    } else {
      res.send("Cita registrada");
    }
  });
};

const modificar = (req, res) => {
  const { id } = req.params;
  const { estado } = req.body;

  const sql = `update cita set estado = '${estado}' where id = ${id}`;

  conexion.run(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error: " + err);
    } else {
      res.send("Cita modificada");
    }
  });
};

const elimnar = (req, res) => {
  const { id } = req.params;

  const sql = `delete from cita where id = ${id}`;

  conexion.run(sql, (err) => {
    if (err) {
      res.send("Ha ocurrido un error: " + err);
    } else {
      res.send("Cita eliminada");
    }
  });
};

module.exports = { todas, buscar, registrar, modificar, elimnar };
