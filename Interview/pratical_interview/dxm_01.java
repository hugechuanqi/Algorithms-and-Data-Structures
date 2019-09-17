   public int cutOffTree(List<List<Integer>> forest) {
        int[][] moves = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        int treeSum = 0;
        int xL = forest.size();
        int yL = forest.get(0).size();

        //初始化available数组，一开始只有起始点和起始点的相邻点可以抵达
        int[][] available = new int[xL][yL];
        available[0][0]=1;
        if(forest.get(0).get(1)>0)
            available[0][1]=1;
        if(forest.get(1).get(0)>0)        
            available[1][0]=1;

        //计算树木总数
        for(int i=0;i<forest.size();i++){
            List<Integer> column = forest.get(i);
            for(int j=0;j<column.size();j++){
                if(column.get(j)>1){
                    treeSum++;
                }
            }
        }
        int step = 0;
        int x=0;
        int y=0;
        
        /**每次循环砍一棵树，直到砍完所有树木，或者没有通往下一棵树的路径*/
        while(true){
            //打印地图
            for(List<Integer> c:forest){
                System.out.println(c);
            }           
            boolean findNextTree=false;
            int height = forest.get(x).get(y);
            int nextX = x;
            int nextY = y;
             //当前位置是树木则砍倒，并将高度设为1
            if(height>1){
                treeSum--;
                forest.get(x).set(y,1);
            }       
            //找到可抵达位置中最矮的那棵树作为目的地/
            int minH = Integer.MAX_VALUE;
            for(int i=0;i<xL;i++){
                for(int j=0;j<yL;j++){
                    int h = forest.get(i).get(j);
                    if(available[i][j]>0&&h>1){
                        if(!findNextTree) 
                            findNextTree=true;
                        if(minH>h){
                            minH=h;
                            nextX=i;
                            nextY=j;
                        } 
                    }
                }
            }
            //如果找不到下一步可以砍的树则退出循环
            if(!findNextTree){
                break;
            }

            //计算通往目的地的最短路径长度，每个点到出发点的距离储存在数组d当中
            int[][] d = new int[xL][yL];
            //距离初始化为-1
            for(int[] ds:d){
                for(int i=0;i<ds.length;i++){
                    ds[i]=-1;
                }
            }
            d[x][y]=0;
            //每一次待计算距离的点储存在trees中，初始化时将出发点存入
            List<Integer> tree = new ArrayList<>();
            tree.add(x);
            tree.add(y);
            List<List<Integer>> trees = new ArrayList<>();
            trees.add(tree);
            
            //计算目标点到本次出发点的距离，增加总步数，将目标点设定为下一步的出发点
            getDistance(trees,forest,d);
            int nextStep = d[nextX][nextY];
            step+=nextStep;
            x=nextX;
            y=nextY;

            //每抵达一个新位置，检查是否增加了可抵达的点
            //新位置周围的四个点如果没有越出边界且不是障碍物，就是新的可抵达点
            for(int[] move:moves){
                int adjacentX = x+move[0];
                int adjacentY = y+move[1];
              if(adjacentX>=0&&adjacentX<xL&&adjacentY>=0&&adjacentY<yL&&forest.get(adjacentX).get(adjacentY)>0){
                    available[adjacentX][adjacentY]=1;
                }
            }
        }

        //如果砍完了所有树则返回总步数，否则返回-1
        if(treeSum==0)
            return step;
        else
            return -1;
}

    /** 计算各点到出发点距离的方法 */
    static void getDistance(List<List<Integer>> trees, List<List<Integer>> forest, int[][] d) {
        int[][] moves = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        int xL = d.length, yL = d[0].length;
        // 储存下一步待计算的点
        List<List<Integer>> newTrees = new ArrayList<>();
        /** 每次循环，计算每个待计算点周围四个点距出发点的距离，并将符合条件的点加入新的待计算List中 */
        for (List<Integer> t : trees) {
            int x = t.get(0);
            int y = t.get(1);
            int currentD = d[x][y];
            for(int[] move:moves){
                int adjacentX = x+move[0];
                int adjacentY = y+move[1];
                /** 如果待计算点不是障碍物或者树木，就将其加入到新的待计算List中 */
                if(adjacentX>=0&&adjacentX<xL&&adjacentY>=0&&adjacentY<yL){
                    int h = forest.get(adjacentX).get(adjacentY);
                    int distance = d[adjacentX][adjacentY];
                    if (h > 0 && distance < 0) {
                        d[adjacentX][adjacentY] = currentD + 1;
                        if (h == 1) {
                            List<Integer> newTree = new ArrayList<>();
                            newTree.add(adjacentX);
                            newTree.add(adjacentY);
                            newTrees.add(newTree);
                        }
                    }
                }
            }        
        }
        trees.clear();
        trees = null;
        if (newTrees.size() > 0) {
            getDistance(newTrees, forest, d);
        }
    