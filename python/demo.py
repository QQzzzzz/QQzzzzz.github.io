from ToolGood.Words.WordsSearch import WordsSearch

def read_keywords_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().splitlines()

if __name__ == "__main__":
    keywords = read_keywords_from_file("dict.txt")

    search = WordsSearch()
    search.SetKeywords(keywords)

    test = input("请输入要查询的文本：")

    # 查找第一个关键词
    f = search.FindFirst(test)
    if f["Keyword"] is None:
        print("WordsSearch FindFirst 出错了......")
    else:
        print(f"FindFirst 找到关键词：{f['Keyword']}，位置：{f['Start']} 到 {f['End']}")

    # 查找所有关键词
    all = search.FindAll(test)
    if not all:
        print("WordsSearch FindAll 出错了......")
    else:
        for match in all:
            print(f"FindAll 找到关键词：{match['Keyword']}，位置：{match['Start']} 到 {match['End']}")

    # 检查是否包含任何关键词
    b = search.ContainsAny(test)
    if not b:
        print("WordsSearch ContainsAny 出错了......")
    else:
        print("ContainsAny 找到关键词")

    txt = search.Replace(test)
    if txt == test:
        print("WordsSearch Replace 出错了......")
    else:
        print(f"替换后的文本：{txt}")
