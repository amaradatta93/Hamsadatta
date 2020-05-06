import { Component, OnInit } from '@angular/core';

import { CategoryviewService } from '../services/categoryview.service';
import { Category } from '../models/category';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  category: Category[];

  constructor(private categoryviewService: CategoryviewService) { }

  ngOnInit() {
    this.getCategory();
  }

  getCategory(): void {
    this.categoryviewService.getCategory()
    .subscribe((category: Category[]) => this.category = category);
  }

}
