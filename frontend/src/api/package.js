import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

export const getPackageList = () => api.get('/packages')
export const getPackageDetail = (id) => api.get(`/packages/${id}`)
