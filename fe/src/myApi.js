import axios from 'axios'
export default axios.create({
  baseURL: 'http://0.0.0.0:8081/',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})