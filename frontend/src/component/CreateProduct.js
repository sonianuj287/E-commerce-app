import React, { useState } from "react";
import axios from "axios";

export default function CreateProduct() {
  const [form, setForm] = useState({
    name: "",
    description: "",
    price: "",
    quantity: "",
  });

  // handle change
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // handle submit
  const handleSubmit = async(e) => {
    e.preventDefault();
    try {
      const API = axios.create({
        baseURL: "http://127.0.0.1:8000/Products/Products/",
      });
        console.log(form);
        const res = await API.post("",form);
        setForm(res.data);
    } catch (err) {
      console.error("Error fetching products:", err);
    }
    // later you can replace this with axios.post() to Django API
  };

  return (
    <div style={{ margin: "20px" }}>
      <h2>➕ Add Product</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Product Name"
          value={form.name}
          onChange={handleChange}
        />
        <br /><br />
        <input
          type="text"
          name="description"
          placeholder="Description"
          value={form.description}
          onChange={handleChange}
        />
        <br /><br />
        <input
          type="number"
          name="price"
          placeholder="Price"
          value={form.price}
          onChange={handleChange}
        />
        <br /><br />
        <input
          type="number"
          name="quantity"
          placeholder="Quantity"
          value={form.quantity}
          onChange={handleChange}
        />
        <br /><br />
        <button type="submit">Add Product</button>
      </form>
    </div>
  );
}
