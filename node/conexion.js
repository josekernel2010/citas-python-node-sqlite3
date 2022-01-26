const sqlite = require("sqlite3");

const conexion = new sqlite.Database("citas.db", (err) => {
  if (err) {
    console.log("Error al conectar a la base de datos", err);
  } else {
    console.log("Conectado a la base de datos");
  }
});

const sql = `create table if not exists cita(
    id integer primary key autoincrement,
    paciente text not null,
    detalle text not null,
    fecha date not null,
    hora time not null,
    estado text not null
    )`;

conexion.run(sql);

module.exports = conexion;
