import React from "react";
import './App.css';
import Card from './card';
import axios from "axios";

const baseURL = "http://127.0.0.1:5000/";

function App() {
  const [content, setContent] =React.useState(null);


  React.useEffect(() => {
    async function fetchData() {
        try {
          axios.get(baseURL).then((response) => {
            setContent(response.data[0].data);
          }
            );
        } catch (e) {
            console.error(e);
        }
    };
    fetchData();
}, []);


  let itemList=[];
  if (content){
    content.map((item)=>{
      itemList.push( <Card title={item.Title} image={item.Image} link={item.Link}></Card>)
    })
  }
  

  return (
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 items-center justify-center bg-indigo-50 px-4">
      {itemList}

    </div>
  );
}

export default App;
