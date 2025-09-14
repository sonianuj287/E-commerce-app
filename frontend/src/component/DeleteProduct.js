import React, { useState } from "react";
import axios from "axios";

export default function DeleteProduct(){


    const [form, setForm] = useState({
        name: "",
      });
    const Delete = async() =>{
        console.log(form);

        try{
        const API = axios.create({
        baseURL: "http://127.0.0.1:8000/Products/Products/",
      });
      const res = await API.delete("", {
        data: { name: form.name }, // send product name in body
      });

      alert("Deleted successfully!");
    }catch (err) {
      console.error("Error fetching products:", err);
    }
}
    return (
    <div>
      <h2>Delete Product</h2>
      <input
        type="text"
        placeholder="Enter product name"
        value={form.name}
        onChange={(e) => setForm({ name: e.target.value })}
      />
      <button onClick={Delete}>Delete</button>
    </div>
  );
}