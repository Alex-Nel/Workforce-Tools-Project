const express = require('express');
const mongoose = require('mongoose');
const app = express();

app.use(express.json());

// DB connection using the service name 'db' defined in docker-compose
const mongoURI = process.env.MONGO_URI || 'mongodb://db:27017/taskdb';

mongoose.connect(mongoURI)
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('Connection error', err));

const Task = mongoose.model('Task', { name: String });

// GET all tasks
app.get('/tasks', async (req, res) => {
  const tasks = await Task.find();
  res.json(tasks);
});

// POST a new task
app.post('/tasks', async (req, res) => {
  const newTask = new Task({ name: req.body.name });
  await newTask.save();
  res.status(201).json(newTask);
});

// DELETE a task
app.delete('/tasks/:id', async (req, res) => {
  await Task.findByIdAndDelete(req.params.id);
  res.status(204).send();
});

app.listen(3000, () => console.log('Server running on port 3000'));
