import { CompleteBankBranch } from "..";

export async function getBranchRequest(
  branchId: number
): Promise<CompleteBankBranch | null> {
  try {
    const response = await fetch("");
    return await response.json();
  } catch (e) {
    return null;
  }
}
