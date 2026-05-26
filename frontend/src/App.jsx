import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [products, setProducts] = useState([])
  const [selected, setSelected] = useState('milk')

  useEffect(() => {
    fetchData(selected)
  }, [selected])

  const fetchData = async (product) => {
    const response = await axios.get(`http://localhost:8000/compare/${product}`)
    setProducts(response.data)
  }
  
  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-4xl font-bold text-center mb-10">
        Aldi vs Lidl Price Comparator
      </h1>

      <div className="flex justify-center mb-8">
        <select
          className="p-3 rounded border"
          onChange={(e) => setSelected(e.target.value)}
        >
          <option value="milk">Milk</option>
          <option value="bread">Bread</option>
          <option value="rice">Rice</option>
        </select>
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        {products.map((item, index) => (
          <div key={index} className="bg-white p-6 rounded shadow-lg">
            <h2 className="text-2xl font-bold">{item.store}</h2>
            <p className="mt-2">Product: {item.product}</p>
            <p className="mt-2">Price: €{item.price}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App

