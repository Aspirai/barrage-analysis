
import axiosInstance from './index'

const axios = axiosInstance

export const getBarrage = () => {return axios.get(`http://localhost:8000/api/ai/`)}