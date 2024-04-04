import './Section2.css';
import CountUp from 'react-countup';


function Section2() {
    const firstEndValue = 11.5;
    const secondEndValue = 21.9
    const thirdEndValue = 0.00025

    return (
        <div className="bg-custom-bg bg-no-repeat bg-cover p-8">
            <div className="mt-5 sm:col md:flex justify-around">
                <div className="text-white">
                    <h1 className="text-4xl mt-12">Join a community</h1>
                    <h1 className="text-4xl">of millions</h1>
                </div>
                <div className="xs:p-2 md:p-8">
                    <div className="flex flex-col">
                        <div>
                            <CountUp className='bg-gradient-1' end={firstEndValue} duration={2} decimals={1} suffix="M+" />
                            <h2 className="text-gray-400 text-transparent text-xl sm:mx-auto">Active Accounts</h2>
                        </div>
                        <div>
                            <CountUp className='bg-gradient-2' end={secondEndValue} duration={2} decimals={1} suffix="M" />
                            <h2 className="text-gray-400 text-transparent text-xl">NFTs minted</h2>
                        </div>
                        <div>
                            <CountUp className='bg-gradient-3' end={thirdEndValue} duration={2} decimals={5} prefix="$" />
                            <h2 className="text-gray-400 text-transparent text-xl">Average cost per transaction</h2>
                        </div>
                    </div>
                </div>
            </div>

            <div className="mt-5 sm:col md:flex justify-around">
                <div className="text-white">
                    <h1 className="text-4xl mt-12">Made For</h1>
                    <h1 className="text-4xl">Mass Adaption</h1>
                    <div className="mt-2 flex items-center">
                        <span className="mt-2 text-white mr-1" style={{ color: "#1FCFF1" }}>*</span>
                        <h1 className="text-gray-400 text-xl">Live data</h1>
                    </div>
                </div>
                <div className="p-8 xs:p-2 flex xs:flex-col md:flex-row">
                    <div className="mt-12 mr-12 flex flex-col">
                        <div class="custom-card p-6 bg-navColor rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                            <span>
                                <h5 class="mt-4 mb-2 text-3xl text-white tracking-tight dark:text-white" style={{ borderLeft: "4px solid #15839b", paddingLeft: '10px' }}>Fast</h5>
                            </span>
                            <p class="mt-4 mb-3 font-normal text-gray-300">Don’t keep your users waiting. Solana has block times of 400 milliseconds — and as hardware gets faster, so will the network.</p>
                            <div className="mt-2 flex items-center">
                                <span className="text-white mr-1" style={{ color: "#1FCFF1" }}>*</span>
                                <p class="mb-3 font-normal text-3xl text-white">3,969</p>
                            </div>
                            <p class="mt-4 mb-3 font-normal text-gray-300">Transactions per second</p>
                        </div>
                        <div class="custom-card mt-6 p-6 bg-navColor rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                            <span>
                                <h5 class="mb-2 text-3xl tracking-tight text-white dark:text-white" style={{ borderLeft: "4px solid #602b9f", paddingLeft: '10px' }}>Scalable</h5>
                            </span>
                            <p class="mt-4 mb-3 font-normal text-gray-300">Get big, quick. Solana is made to handle thousands of transactions per second, and fees for both developers and users remain less than $0.01.</p>
                            <div className="mt-2 flex items-center">
                                <span className="text-white mr-1" style={{ color: "#1FCFF1" }}>*</span>
                                <p class="mb-3 font-normal text-3xl text-white">163,077,581,394</p>
                            </div>
                            <p class="mb-3 font-normal text-gray-300">Total transactions</p>
                        </div>
                    </div>
                    <div className="flex flex-col">
                        <div class="custom-card p-6 bg-navColor rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                            <span>
                                <h5 class="mt-4 mb-2 text-3xl tracking-tight text-white dark:text-white" style={{ borderLeft: "4px solid #bfa00e", paddingLeft: '10px' }}>Decentralized</h5>
                            </span>
                            <p class="mt-4 mb-3 font-normal text-gray-300">The Solana network is validated by thousands of nodes that operate independently of each other, ensuring your data remains secure and censorship resistant.</p>
                            <div className="mt-2 flex items-center">
                                <span className="text-white mr-1" style={{ color: "#1FCFF1" }}>*</span>
                                <p class="mb-3 font-normal text-3xl text-white">1,675</p>
                            </div>
                            <p class="mb-3 font-normal text-white text-gray-300">Validator nodes</p>
                        </div>
                        <div class="custom-card mt-6 p-6 bg-navColor  rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                            <span>
                                <h5 class="mt-4 mb-2 text-white text-3xl tracking-tight" style={{ borderLeft: "4px solid #13be75", paddingLeft: '10px' }}>Energy Efficient</h5>
                            </span>
                            <p class="mt-4 mb-3 font-normal text-gray-300">Solana’s proof of stake network and other innovations minimize its impact on the <a href="https://solana.com" className="underline" style={{ color: "#1FCFF1" }}>environment.</a> Each Solana transaction uses about the same energy as a few Google searches.</p>
                            <p class="mb-3 font-normal text-white text-3xl">0%</p>
                            <p class="mb-3 font-normal text-gray-300">Net carbon impact</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};
export default Section2;