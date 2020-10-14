int ans;
int height (TreeNode* root) {
if (!root)
return 0;
return max(height(root->left), height(root->right)) + 1;
}

int solveUtil (TreeNode* root, bool *flag, int B) { // working function
    if (!root)
        return 0;

    if (root->val == B) {
        ans = max(ans, max(height(root->left), height(root->right)));
        (*flag) = true;
        return 0;
    }

    bool l = false, r = false;
    int left = solveUtil(root->left, &l, B);
    int right = solveUtil(root->right, &r, B);

    if (l || r) {
        (*flag) = true;
        ans = max(ans, left + right + 1);
        if (l)
            return left + 1;
        else
            return right + 1;
    }

    return max(left, right) + 1;

}

int Solution::solve(TreeNode* A, int B) {       // main starting function
ans = 0;
bool flag = false;
solveUtil(A, &flag, B);
return ans;
}