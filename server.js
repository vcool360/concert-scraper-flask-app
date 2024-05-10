const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost/ticket_tracker', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
    .then(() => console.log("MongoDB successfully connected"))
    .catch(err => console.log(err));

// MongoDB schema and model
const TicketSchema = new mongoose.Schema({
    event: String,
    prices: [Number],
    dateScraped: { type: Date, default: Date.now }
});

const Ticket = mongoose.model('Ticket', TicketSchema);

// Routes
app.get('/', (req, res) => {
    res.send('Ticket Price Tracker API is running!');
});

// Post ticket data
app.post('/tickets', (req, res) => {
    const newTicket = new Ticket({
        event: req.body.event,
        prices: req.body.prices,
        dateScraped: req.body.dateScraped
    });

    newTicket.save()
        .then(ticket => res.json(ticket))
        .catch(err => res.status(400).json('Error: ' + err));
});

// Get all tickets
app.get('/tickets', (req, res) => {
    Ticket.find()
        .then(tickets => res.json(tickets))
        .catch(err => res.status(400).json('Error: ' + err));
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
