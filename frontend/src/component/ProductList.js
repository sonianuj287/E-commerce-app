import React, { useEffect, useState } from "react";
import axios from "axios";


export default function ProductList(){

    const [products, setProducts]= useState([]);

    const fetchProducts = async () => {
    try {
      const API = axios.create({
        baseURL: "http://127.0.0.1:8000/Products/Products/",
      });
      const res = await API.get("");
      setProducts(res.data);
    } catch (err) {
      console.error("Error fetching products:", err);
    }
  };

   useEffect(() => {
    fetchProducts();
  }, []);


    return (  
        <div>
            <ul>
             {products.map((p, i) => (
             <li key={i}>
            {p.name} - {p.price}₹ ({p.quantity} pcs) ---({p.description})
            </li>
        ))}
      </ul>
        </div>
    )

}