import React from "react";
import './App.css';
import Card from './card';
import axios from "axios";

const baseURL = "http://127.0.0.1:5000/";

function App() {
  const [title, setTitle] = React.useState(null);
  const [link, setLink] = React.useState(null);
  const [image, setImage] = React.useState(null);


  React.useEffect(() => {
    async function fetchData() {
        try {
          axios.get(baseURL).then((response) => {
            setTitle(response.data[0].data['Title']);
            setLink(response.data[0].data['Link']);
            setImage(response.data[0].data['Image']);
            // console.log(response.data[0].data['Title'][2]);
          }
            );
        } catch (e) {
            console.error(e);
        }
    };
    fetchData();
}, []);


  let items=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19];
  let itemList=[];
  items.forEach((item)=>{
    itemList.push( <Card title={title[item]} image={image[item]} link={link[item]}></Card>)
  })

  // if (!post) return null;
  return (
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 items-center justify-center bg-indigo-50 px-4">
      {console.log(title)}
      {itemList}

    </div>
  );
}

export default App;
