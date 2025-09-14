import logo from './logo.svg';
import './App.css';
import ProductList from './component/ProductList';
import CreateProduct from './component/CreateProduct';
import DeleteProduct from './component/DeleteProduct';

function App() {
  return (
    <div className="App">
      <p>this is me and my life by sneha </p>
      <ProductList/>
      <CreateProduct/>
      <DeleteProduct/>

    </div>
  );
}

export default App;
