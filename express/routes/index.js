import express from 'express'
import models from '../models'

let router = express.Router()

router.get('/', (req, res, next) => {
  res.render('index', {
    title: 'Index'
  })
})

export default router
