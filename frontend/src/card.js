import React from 'react'

function Card(props) {
  return (
  <div class="max-w-sm overflow-hidden rounded-xl bg-white shadow-md duration-200 hover:scale-105 hover:shadow-xl m-4">
    <img src={props.image} class="h-auto w-full" />
    <div class="p-5">
      <p class="text-medium mb-5 text-gray-700">{props.title}</p>
      <a href={props.link} class="w-full p-4 rounded-md bg-indigo-600  py-2 text-indigo-100 hover:bg-indigo-500 hover:shadow-md duration-75">Read Now</a>
    </div>
  </div>

  )
}

export default Card