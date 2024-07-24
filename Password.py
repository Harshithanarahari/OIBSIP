{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "26334b5d-6f08-44e4-a4de-e2ed48e30b04",
   "metadata": {},
   "source": [
    "**Password Generator**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0be273ec-f607-4792-959c-fb4bb971d163",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How many character you want:  5\n",
      "How many integer you want:  4\n",
      "How many symbol you want:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Generated password:  S42Tm3i<6V%\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import string\n",
    "\n",
    "char_lis = list(string.ascii_letters)\n",
    "num_lis = list(string.digits)\n",
    "symbols = list(string.punctuation)\n",
    "\n",
    "password_lis = []\n",
    "\n",
    "num_of_char = int(input(\"How many character you want: \"))\n",
    "num_of_integer = int(input(\"How many integer you want: \"))\n",
    "num_of_symbol = int(input(\"How many symbol you want: \"))\n",
    "\n",
    "for char in range(1,num_of_char+1):\n",
    "    password_lis.append(random.choice(char_lis))\n",
    "\n",
    "for int in range(1,num_of_integer+1):\n",
    "    password_lis.append(random.choice(num_lis))\n",
    "\n",
    "for sym in range(1,num_of_symbol+1):\n",
    "    password_lis.append(random.choice(symbols))\n",
    "\n",
    "Password = \"\"\n",
    "random.shuffle(password_lis)\n",
    "\n",
    "for i in password_lis:\n",
    "    Password = f\"{Password}{i}\"\n",
    "\n",
    "print()\n",
    "print(\"Generated password: \",Password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9556e134-7ba0-47e4-a20b-9f5716b241e9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
