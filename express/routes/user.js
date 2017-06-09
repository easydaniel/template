import express from 'express'
import models from '../models'
import bcrypt from 'bcrypt'

let router = express.Router()

router.get('/', (req, res, next) => {
  res.render('index', {
    title: 'User'
  })
})

router.get('/list', (req, res, next) => {
  models.User
    .findAll()
    .then((users) => {
      res.json(users);
    });
})

router.post('/create', async (req, res, next) => {
  let user = await models.User
    .findOne({
      where: {
        username: req.body.username
      }
    })
  if (!user) {
    models.User
      .create({
        username: req.body.username,
        password: bcrypt.hashSync(req.body.password, bcrypt.genSaltSync(10))
      })
      .then(() => {
        res.redirect('/user/list')
      })
  } else {
    res.send('user exists')
  }
})

router.get('/delete/:id', (req, res, next) => {
  models.User
    .destroy({
      where: {
        id: req.params.id
      }
    })
    .then(() => {
      res.redirect('/user/list')
    })
})

export default router
