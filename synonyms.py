import math

def norm(vec):
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

# Part a)
def cosine_similarity(vec1, vec2):
    keys1 = set(vec1.keys())
    keys2 = set(vec2.keys())
    shared = keys1.intersection(keys2)

    numerator = 0
    for key in shared:
        numerator += vec1[key] * vec2[key]
    
    values1 = list(vec1.values())
    sum1 = 0
    values2 = list(vec2.values())
    sum2 = 0
    for value in values1:
        sum1 += value ** 2
    for value in values2:
        sum2 += value ** 2

    denom = math.sqrt(sum1 * sum2)

    return numerator / denom

def build_semantic_descriptors(sentences):
    sets = []
    for i in range(len(sentences)):
        sets.append(set(sentences[i]))
    
    sol_dict = dict()
    for words in sets:
        for word in words:
            if not(word in sol_dict.keys()):
                sol_dict[word] = dict()

    for words in sets:
        for w1 in words:
            for w2 in words:
                if w1 in sol_dict[w2].keys():
                    sol_dict[w2][w1] += 1
                else:
                    sol_dict[w2][w1] = 1

    for key in sol_dict.keys():
        del sol_dict[key][key]

    return sol_dict

# Part c)
def build_semantic_descriptors_from_files(filenames):
    text = ""
    for file in filenames:
        text += open(file, "r", encoding="latin1").read()

    text = text.replace(", ", " ")
    text = text.replace("-", " ")
    text = text.replace("--", " ")
    text = text.replace(":", " ")
    text = text.replace(";", " ")
    text = text.replace("! ",".")
    text = text.replace("? ", ".")
    text = text.replace(". ", ".")
    text = text.lower()
    text = text.split(".")
    while "" in text:
        text.remove("")

    for i in range(len(text)):
        temp = text[i].split()
        text[i] = temp
    
    result = build_semantic_descriptors(text)

    return result

# Part d)
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max_sim = -1
    max_sim_index = 0
    base = semantic_descriptors[word]
    for i in range(len(choices)):
        if choices[i] not in semantic_descriptors.keys():
            continue
        sim = similarity_fn(semantic_descriptors[choices[i]], base)
        if sim > max_sim:
            max_sim = sim
            max_sim_index = i
    return choices[max_sim_index]

# Part e)
def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    text = ""
    text = open(filename, "r", encoding = "latin1").read()
    text = text.split("\n")
    text.pop(len(text)-1)
    n = len(text)
    count_sum = 0

    for test in text:
        evals = test.split()
        m_sim = most_similar_word(evals[0], evals[2:], semantic_descriptors, similarity_fn)
        if m_sim == evals[1]:
            count_sum += 1
    return count_sum * 100/n