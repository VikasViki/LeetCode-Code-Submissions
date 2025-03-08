class Solution:

    def justify_line(self, index, justified, is_last_line, max_width):
        line = justified[index]
        line_len = len(line)
        line = line + (" " * (max_width-line_len))
        space_count = 0
        for char in line:
            if char == " ":
                space_count += 1
        
        justified_line = line

        if not is_last_line:
            line_split = line.split()
            words_count = len(line_split)
            if words_count-1 != 0:
                common_space = (space_count // (words_count-1))
                rem_space = space_count % common_space
                # print(line_split, space_count, common_space, rem_space)
                spaces = [ common_space ] * (words_count-1)
                space_count -= (common_space * (words_count-1))
                while space_count:
                    for space_index in range(len(spaces)):
                        spaces[space_index] += 1
                        space_count -= 1
                        if space_count == 0:
                            break
                
                justified_line = ""
                for word, space in zip(line_split, spaces):
                    justified_line += word + (" " * space)
                justified_line += line_split[-1]
            
        
        justified[index] = justified_line[:max_width]


    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified = []
        curr_line = ""
        curr_line_len = 0

        for word in words:
            word_len = len(word)

            if (curr_line_len + word_len + 1) <= maxWidth:
                curr_line += word + " "
                curr_line_len += word_len + 1

            elif (curr_line_len + word_len) == maxWidth:
                curr_line += word
                curr_line_len = word_len
                justified.append(curr_line)
                curr_line = ""
                curr_line_len = 0

            else:
                justified.append(curr_line)
                curr_line = word + " "
                curr_line_len = word_len + 1
        
        justified.append(curr_line)
        justified_len = len(justified)
        is_last_line = False
        for index, line in enumerate(justified):
            if index == justified_len-1:
                is_last_line = True
            self.justify_line(index, justified, is_last_line, maxWidth)
        
        if justified[-1].strip() == "":
            justified.pop()

        return justified
            
            
