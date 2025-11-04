import { rpc } from "@cityofzion/neon-js";

const contractHash = "0xcc10840cceebe12b70b088c57102235e2a671d94";
const nodeUrl = "http://localhost:50012";

const client = new rpc.RPCClient(nodeUrl);

async function getTasks() {
  const result = await client.invokeFunction(contractHash, "get_task");
  console.log(result.stack);
}

getTasks();