
function Section1() {
    return (
        <>
        <div className="absolute inset-0 bg-right bg-contain bg-no-repeat" style={{ backgroundImage: "url('./assets/circle-right.svg')",zIndex: -10  }}></div>
      <div className="absolute inset-0 bg-left h-3/4  bg-contain bg-no-repeat " style={{ backgroundImage: "url('./assets/circle-left.svg')", zIndex: -10 }}></div>
        <section className="relative text-center pb-5 flex flex-col items-center  justify-center" style={{ marginTop: '10rem' }}>
            <h1 className="text-3xl md:text-5xl text-white mt-5 lg:text-5xl xl:text-6xl">Powerful for developers.</h1>
            <h1 className="text-3xl md:text-4xl text-white lg:text-5xl xl:text-6xl">Fast for everyone.</h1>
            <p className='text-white p-5'> Bring blockchain to the people. Solana supports experiences for power users, new consumers, and everyone in between.</p>
            <div className="flex justify-center mt-5">
                <button className="bg-gradient hover:bg-gradient text-white py-2 px-4 rounded-full mr-2">START BUILDING</button>
                <button className="bg-black hover:bg-black text-white   border border-white  py-2 px-4 rounded-full">READ DOCS</button>
            </div>
        </section>
        </>
    )
};
export default Section1;