// Implements a dictionary's functionality
# include <stdio.h>
# include <stdlib.h>
# include <stdbool.h>
# include <string.h>
# include <ctype.h>
# include <limits.h>

# include "dictionary.h"



// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

int word_count = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // get lowercase for case-insensitivity
    char no_upper[LENGTH + 1];
    int word_length = strlen(word);
    no_upper[word_length] = '\0';

    // iterate to convert to lower
    for (int i = 0; i < word_length; i++)
    {
        no_upper[i] = tolower(word[i]);
    }

    // hash word to a number
    int index = hash(no_upper);

    // make a pointer to iterate the linked list
    node* pointer = table[index];

    // iterate the linked list to match words
    while (pointer != NULL)
    {
        // compare words
        if (strcmp(no_upper, pointer->word) == 0)
        {
            return true;
        }

        // loop the hashtable
        pointer = pointer->next;

    }

    // return false if no words
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // hash word to a number
    // saw this implementation on github
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // load the dictionary file
    FILE* file = fopen(dictionary, "r");

    // check if file is null
    if (!file)
    {
        printf("Dictionary doest not exist\n");
        return false;
    }

    // temp to not break the linked list
    char tmp[LENGTH + 1] = "\0";

    // scan the file to load
    while (fscanf(file, "%s", tmp) != EOF)
    {
        // load words in to memory
        node *words = malloc(sizeof(node));

        // set next node to NULL
        words->next = NULL;

        // copy the words to the node thank you people of discord
        strcpy(words->word, tmp);

        // create a hash index
        int index = hash(tmp);

        // enter word into hashtable (if empty)
        if (table[index] == NULL)
        {
            table[index] = words;
            words->next = NULL;
        }

        // thank you people of discord
        else
        {
            words->next = table[index];
            table[index] = words;
        }

        // increase the word count for size function
        word_count++;
    }

    // close the file
    fclose(file);

    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // returns word count or 0
    if (word_count > 0)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // free memory
    int i = 0;
    while (table[i] != NULL && i < INT_MAX)
    {
        node* deletor = table[i];
        table[i] = deletor->next;
        free(deletor);
        i++;
    }
    return true;
}
