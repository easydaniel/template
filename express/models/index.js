import fs from 'fs'
import path from 'path'
import config from '../config'
import Sequelize from 'sequelize'

let env = process.env.NODE_ENV || "development";
let sequelize = new Sequelize(config[env].database, config[env].username, config[env].password, config[env])
let db = {}
fs.readdirSync(__dirname)
  .filter((file) => (file.indexOf(".") !== 0) && (file !== "index.js"))
  .forEach((file) => {
    let model = sequelize.import(path.join(__dirname, file))
    db[model.name] = model
  })
Object.keys(db).forEach((modelName) => {
  if ("associate" in db[modelName]) {
    db[modelName].associate(db);
  }
})

db.sequelize = sequelize
db.Sequelize = Sequelize

export default db
