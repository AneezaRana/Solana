import { AiOutlineMenu } from 'react-icons/ai';
import React, { useState } from 'react'
const Header = () => {
  let Links = [
    { name: "Learn", link: "/" },
    { name: "Build", link: "/" },
    { name: "Network", link: "/" },
    { name: "Comunity", link: "/" },
  ];
  let [open, setOpen] = useState(false);
  return (
    <div className='shadow-md  relative  left-0'>
      <div className='md:flex items-center justify-between bg-navColor py-4 md:px-20 px-10'>
        <div className=' cursor-pointer flex items-center'>
          <span className='mr-1 pt-2  '>
            <img src="./assets/logo.svg" alt="Logo" />
          </span>
        </div>
        <div onClick={() => setOpen(!open)} className='text-18 absolute right-8 top-6 cursor-pointer md:hidden'>
          <AiOutlineMenu size={28} name={open ? 'close' : 'menu'} className='lg:hidden text-primary' />
        </div>
        <ul className={`md:flex md:items-center bg-black md:pb-0 pb-12 absolute md:static text-17 md:z-auto z-[-1] left-0  md:w-auto md:pl-0 pl-9 transition-all duration-500 ease-in ${open ? 'top-20 ' : 'top-[-490px]'}`}>
          {
            Links.map((link) => (
              <li key={link.name} className='md:ml-8 text-18 md:my-0 my-7'>
                <a href={link.link} className='text-primary text-17 hover:text-gray-400 duration-500'>{link.name}</a>
              </li>
            ))
          }
        </ul>
      </div>
    </div>
  )
}


export default Header