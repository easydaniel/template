export default (sequelize, DataTypes) => {
  let User = sequelize.define("User", {
    username: DataTypes.STRING,
    password: DataTypes.STRING
  }, {
    classMethods: {
      
    }
  });

  return User;
};
